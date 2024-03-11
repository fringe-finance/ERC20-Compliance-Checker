import requests
import csv
import pysnooper
import traceback
import json
import os
import dotenv
from web3 import Web3

dotenv.load_dotenv()


def getTokenName(contract_address, chain_name):
    chainDetails = json.loads(open(getAbsPath("contracts.json")).read())
    mapping = json.loads(open(getAbsPath("tokenAddressToName.json")).read())
    if contract_address in mapping:
        return mapping[contract_address]
    rpcUrl = chainDetails[chain_name]["rpc"]
    # Create a Web3 instance using the provided RPC endpoint
    w3 = Web3(Web3.HTTPProvider(rpcUrl))

    # Load the ERC20 ABI (Application Binary Interface)
    erc20_abi = [
        {
            "constant": True,
            "inputs": [],
            "name": "name",
            "outputs": [{"name": "", "type": "string"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "symbol",
            "outputs": [{"name": "", "type": "string"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
    ]

    # Create a contract instance using the provided contract address and ABI
    contract = w3.eth.contract(address=contract_address, abi=erc20_abi)
    name = None
    symbol = None
    try:
        name = contract.functions.name().call()
    except:
        pass
    if not name:
        try:
            symbol = contract.functions.symbol().call()
        except:
            pass
    output = name if name else symbol
    with open(getAbsPath("tokenAddressToName.json"), "w") as file:
        mapping[contract_address] = output
        file.write(json.dumps(mapping, indent=4, sort_keys=True))
    return output


def getConfig():
    config_path = getAbsPath("config.json")
    with open(config_path, "r") as file:
        config = json.load(file)
    return config


def dictGet(dictionary, key, default=None):
    value = dictionary.get(key)
    if value is None:
        return default
    return value


def getAbsPath(relPath):
    basepath = os.path.dirname(__file__)
    fullPath = os.path.abspath(os.path.join(basepath, relPath))
    return fullPath


def getErcxErrorDescription(ercxError):
    # Fetch new error description from the API
    url = (
        "https://ercx.runtimeverification.com/api/v1/property-tests?standard=ERC20&name="
        + ercxError
    )

    response = requests.get(url)

    # Ensure that the request was successful
    if response.status_code == 200:
        description = (
            response.json()[0]["feedback"]
            if response.json()
            else camel_to_space_lower(ercxError) + " [[[not found]]]"
        )

        return description
    else:
        return f"Error fetching description: HTTP {response.status_code}"


def camel_to_space_lower(input_string):
    output_string = ""
    for i, char in enumerate(input_string):
        if char.isupper() and i != 0:
            output_string += " " + char.lower()
        else:
            output_string += char.lower()
    return output_string.capitalize()


def saveErcxReport(contract_address, network_id, standard="ERC20"):
    # Determine the file path for saving the report
    outputFilePath = getAbsPath(
        "reports/ercx_report_" + str(contract_address) + ".json"
    )

    if os.path.exists(outputFilePath):
        return
    url = "https://ercx.runtimeverification.com/api/v1/reports"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    data = {
        "standard": standard,
        "address": contract_address,
        "network": int(network_id),
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if "status" not in response.json():
        print(
            "error requesting creation of report for contract",
            contract_address,
            "\nRequest url:\n",
            url,
            "\nHeaders:\n",
            headers,
            "\nPostData\n",
            data,
            "\n\nResponse:\n",
            response.json(),
            "\n\n\n\n",
        )
        return
    if response.json()["status"] == "RUNNING":
        print("report for contract", contract_address, "is still being processed")
        return

    url = f"https://ercx.runtimeverification.com/api/v1/tokens/{network_id}/{contract_address}/report"
    params = {"fields": "json", "standard": standard}
    headers = {
        "accept": "application/json",
        "X-API-KEY": os.environ.get("ERCX_API_KEY"),
    }
    response = requests.get(url, params=params, headers=headers)

    # Check for successful response
    if response.status_code != 200 or response.json()["status"] == "ERROR":
        print(
            "error fetching report for contract",
            contract_address,
            "\n\nRequest url:\n",
            url,
            "\n\nHeaders:\n",
            headers,
            "\n\nPostData\n",
            params,
            "\n\nResponse:\n",
            response.json(),
            "\n\n\n\n",
        )
        return

    data = response.json()
    jsonOutput = json.loads(data["json"])
    feedbacks = data["feedback"]
    saveOutput = {"json": jsonOutput, "feedback": feedbacks}
    with open(outputFilePath, "w") as file:
        print("saving report for contract", contract_address)
        file.write(json.dumps(saveOutput, indent=4, sort_keys=True))


def saveDeDotFiReport(contract_address, network_id):
    outputFilePath = getAbsPath(
        "reports/defi_report_" + str(contract_address) + ".json"
    )

    if os.path.exists(outputFilePath):
        return
    else:
        with open(outputFilePath, "w") as file:
            file.write("{}")
    headers = {
        "authority": "api-scanner.defiyield.app",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-GB,en;q=0.5",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://de.fi",
        "pragma": "no-cache",
        "referer": "https://de.fi/",
        "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }

    graphql_query = {
        "query": """query {
              project(address: \""""
        + contract_address
        + """" networkId: """
        + network_id
        + """ ){
                inProgress
                isProxyImplementation
                proxyContractAddress
                firstTxBlock
                estimatedAnalyzingTime
                address
                network
                rektLink
                name
                contractName
                sourceCodeLink
                whitelisted
                firstTxFrom
                firstTxDate
                logo
                projectName
                projectFullName
                initialFunder
                protocol
                pairInfo {
                  factory
                  tokens {
                    address
                    name
                    symbol
                    score
                    logo
                  }
                }
                coreIssues {
                  scwTitle
                  scwDescription
                   scwId
                  issues {
                    id
                    impact
                    description
                    data
                    snippet
                    start
                    end
                    additionalData {
                      title
                      description
                    }
                    governanceInfo {
                      owners {
                        timelockDelay
                        type
                        owner
                      }
                      worstOwner {
                        timelockDelay
                        type
                        owner
                      }
                    }
                    severityChanges {
                      from
                      to
                      reason
                    }
                  }
                }
                generalIssues {
                  scwTitle
                  scwDescription
                  scwId
                  issues {
                    id
                    confidence
                     impact
                    description
                    snippet
                    start
                    end
                    additionalData {
                      title
                      description
                    }
                    governanceInfo {
                      owners {
                        timelockDelay
                        type
                        owner
                      }
                      worstOwner {
                        timelockDelay
                        type
                        owner
                      }
                    }
                    severityChanges {
                      from
                      to
                      reason
                    }
                  }
                }
                stats {
                  percentage
                  scammed
                }
                diffs {
                    id
                    address
                    network
                    name
                    projectName
                    score
                    createdAt
                  }
                proxyData {
                  sourceCodeLink
                  proxyOwner
                  proxyIssues {
                    scwTitle
                    scwDescription
                    scwId
                    issues {
                      id
                      impact
                      description
                      snippet
                      start
                      end
                      additionalData {
                        title
                        description
                      }
                      governanceInfo {
                        owners {
                          timelockDelay
                          type
                          owner
                        }
                        worstOwner {
                          timelockDelay
                          type
                          owner
                        }
                      }
                      severityChanges {
                        from
                        to
                        reason
                      }
                    }
                  }
                  implementationData {
                    firstTxFrom
                    firstTxDate
                    firstTxBlock
                    name
                    initialFunder
                    initialFunding
                  }
                }
                governance {
                visibleOwner
                proxyOwners {
                  type
                  owner
                  timelockDelay
                  timelock
                  modifiable
                  impact
                  governance {
                    proposals
                    proposalMaxActions
                    votingPeriod
                    quorum
                    threshold
                    name
                  }
                  multisig {
                    threshold
                    transactionCount
                    multisigOwners
                  }
                }
                contractOwners {
                  type
                  owner
                  timelockDelay
                  timelock
                  modifiable
                  impact
                  governance {
                    proposals
                    proposalMaxActions
                    votingPeriod
                    quorum
                    threshold
                    name
                  }
                  multisig {
                    threshold
                    transactionCount
                    multisigOwners
                  }
                }
                issueOwners {
                  scwId
                  owners {
                    type
                    owner
                    timelockDelay
                    timelock
                    modifiable
                    impact
                    governance {
                      proposals
                      proposalMaxActions
                      votingPeriod
                      quorum
                      threshold
                      name
                    }
                  multisig {
                    threshold
                    transactionCount
                    multisigOwners
                  }
                  }
                }
              }
              }
            }
        """
    }

    response = requests.post(
        "https://api-scanner.defiyield.app/", headers=headers, json=graphql_query
    )

    if response.status_code != 200:
        print(
            f"Failed to fetch data: {response.text} for token {contract_address} with de.fi"
        )
        return

    data = response.json()
    reportOutput = json.dumps(data, indent=4, sort_keys=True)

    with open(outputFilePath, "w") as file:
        file.write(reportOutput)


def getIssueDetails(issueId, sourceAPI, issueDescription):
    with open(getAbsPath("issueClassification.json")) as file:
        issueClassification = json.load(file)
    if not issueId in issueClassification["issues"]:
        if sourceAPI == "de.fi":
            description = issueDescription
            issueClass = "undetermined"
        elif sourceAPI == "ercx":
            description = getErcxErrorDescription(issueId)
            issueClass = "undetermined"
        issueClassification["issues"][issueId] = {
            "description": description,
            "class": issueClass,
        }
        with open(getAbsPath("issueClassification.json"), "w") as file:
            json.dump(issueClassification, file, indent=4, sort_keys=True)

    issue = issueClassification["issues"][issueId]
    issueClass = issue["class"]
    issueDescription = issue["description"]
    classIsActive = (
        issueClass and issueClassification["categories"][issueClass]["active"]
    )
    if classIsActive:
        return issueClass, issueDescription
    return None, None


def filterIssues(issues, sourceAPI):
    filtered_issues = {}
    for issueId, issueDescription in issues:
        issueClass, issueDescription = getIssueDetails(
            issueId, sourceAPI, issueDescription
        )
        if not issueClass or not issueDescription:
            continue
        issueString = f"{sourceAPI} | {issueDescription}"
        if issueClass not in filtered_issues:
            filtered_issues[issueClass] = []
        filtered_issues[issueClass].append(issueString)

    return filtered_issues


def saveIssuesForToken(contract_address, chain_name):
    issues = {}
    try:
        defiPath = getAbsPath("reports/defi_report_" + str(contract_address) + ".json")
        defiReport = json.load(open(defiPath))
        for category in ["coreIssues"]:  ##, "generalIssues"]:
            failedTestIds = (
                [
                    [issue["scwId"], issue["scwDescription"]]
                    for issue in defiReport["data"]["project"][category]
                    if issue["issues"]
                ]
                if defiReport["data"]["project"][category]
                else []
            )
            issues.update(filterIssues(failedTestIds, "de.fi"))

        implementation_data_name = dictGet(
            dictGet(
                dictGet(
                    dictGet(dictGet(defiReport, "data", {}), "project", {}),
                    "proxyData",
                    {},
                ),
                "implementationData",
                {},
            ),
            "name",
        )

    except Exception as e:
        print("errr when loading defi report: ", e)
        traceback.print_exc()

    try:
        ercxPath = getAbsPath("reports/ercx_report_" + str(contract_address) + ".json")
        if os.path.exists(ercxPath):
            ercxReport = json.load(open(ercxPath))
            jsonOutput, feedback = ercxReport["json"], ercxReport["feedback"]
            testCategories = [
                "test/ERC20Minimal.t.sol:ERC20Minimal",
                "test/ERC20Recommended.t.sol:ERC20Recommended",
                "test/ERC20Desirable.t.sol:ERC20Desirable",
            ]
            for category in testCategories:
                if category not in jsonOutput:
                    continue
                testResults = jsonOutput[category]["test_results"]
                failedTestIds = [
                    [testName.split("(")[0], None]
                    for testName in testResults
                    if "status" not in testResults[testName]
                    or testResults[testName]["status"] != "Success"
                ]
                issues.update(filterIssues(failedTestIds, "ercx"))
        else:
            print("no ercx report found for contract: ", contract_address)

    except Exception as e:
        print("errr when loading ercx report: ", e)
        traceback.print_exc()

    failedTestsFile = json.load(open(getAbsPath("failedTests.json")))
    if chain_name not in failedTestsFile:
        failedTestsFile[chain_name] = {}

    failedTestsFile[chain_name][contract_address] = {
        "name": getTokenName(contract_address, chain_name),
        "issues": issues,
    }
    with open(getAbsPath("failedTests.json"), "w") as file:
        file.write(json.dumps(failedTestsFile, indent=4, sort_keys=True))


def getExplorerUrl(contract_address, chain_name):
    chainDetails = json.loads(open(getAbsPath("contracts.json")).read())
    explorerBaseUrl = chainDetails[chain_name]["explorerBaseUrl"]
    explorerUrl = f"{explorerBaseUrl}/address/{contract_address}#code"
    return explorerUrl


def json_to_markdown_report(json_file_path, markdown_file_path):
    with open(json_file_path, "r") as file:
        data = json.load(file)
    markdown_report = ""
    for chain in data:
        markdown_report += f"\n\n\n\n\n# {chain}\n\n"
        for address, details in sorted(data[chain].items()):
            issues = details.get("issues", {})
            projectName = details.get("name", "")
            explorerUrl = getExplorerUrl(address, chain)
            if issues:
                markdown_report += f"\n\n### {projectName}\n"
                markdown_report += f"**Address:** {address}\n"
                markdown_report += f"**Explorer url:** {explorerUrl}\n\n"

                markdown_report += "##### Issue Categories\n"
                for category in issues.keys():
                    markdown_report += f"###### {category}\n"
                markdown_report += "\n"
                for issueClass, issueList in issues.items():
                    if issueList:
                        markdown_report += f"###### {issueClass} Issues\n"
                    for issue in issueList:
                        markdown_report += f"- {issue}\n"
                    markdown_report += "\n"

    with open(markdown_file_path, "w") as file:
        file.write(markdown_report)


def json_to_csv_report(json_file_path, csv_file_path):
    with open(json_file_path, "r") as file:
        data = json.load(file)

    issue_categories = set()
    for chain in data:
        for details in data[chain].values():
            issues = details.get("issues", {})
            issue_categories.update(issues.keys())

    issue_categories = sorted(issue_categories)

    with open(csv_file_path, "w", newline="") as file:
        writer = csv.writer(file)
        header = ["Token", "Explorer URL"] + issue_categories
        writer.writerow(header)

        for chain in data:
            for address, details in data[chain].items():
                issues = details.get("issues", {})
                project_name = details.get("name", "")
                explorer_url = getExplorerUrl(address, chain)

                row = [chain + " | " + project_name, explorer_url]
                for category in issue_categories:
                    if category in issues:
                        row.append("x")
                    else:
                        row.append("")

                writer.writerow(row)


def main():
    contracts_path = getAbsPath("contracts.json")
    with open(contracts_path, "r") as file:
        contracts = json.load(file)
    for network in contracts:
        chain_name = network
        network_id = contracts[network]["network_id"]
        addresses = contracts[network]["contracts"]
        for contract_address in addresses:
            saveErcxReport(contract_address, network_id)
            saveDeDotFiReport(contract_address, network_id)
            saveIssuesForToken(contract_address, chain_name)
    json_to_markdown_report(getAbsPath("failedTests.json"), getAbsPath("report.md"))
    json_to_csv_report(getAbsPath("failedTests.json"), getAbsPath("report.csv"))


if __name__ == "__main__":
    main()
