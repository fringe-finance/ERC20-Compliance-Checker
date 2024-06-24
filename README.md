# ERC20 Security Analysis Script

This script analyzes ERC20 token security and spec-compliance across multiple blockchain networks, fetching reports from ERCX and De.Fi, and generating a consolidated report of issues.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`, `web3`, `python-dotenv`, `pysnooper`

## Setup

1. Clone the repository or download the script.

2. Install required packages:
   ```
   pip install requests web3 python-dotenv pysnooper
   ```

3. Create a `.env` file in the same directory as the script and add your ERCX API key:
   ```
   ERCX_API_KEY=your_api_key_here
   ```

4. Ensure the following JSON files are present in the script's directory:
   - `contracts.json`: Contains network details and token addresses to analyze
   - `issueClassification.json`: Classification of issues

## Usage

1. Update `contracts.json` with the networks and token addresses you want to analyze. Example format:
   ```json
   {
     "ethereum": {
       "network_id": "1",
       "rpc": "https://ethereum-rpc-url",
       "explorerBaseUrl": "https://etherscan.io",
       "contracts": ["0x123...", "0x456..."]
     },
     "bsc": {
       "network_id": "56",
       "rpc": "https://bsc-rpc-url",
       "explorerBaseUrl": "https://bscscan.com",
       "contracts": ["0x789...", "0xabc..."]
     }
   }
   ```

2. Run the script:
   ```
   python script_name.py
   ```

3. The script will:
   - Fetch ERCX reports for each token (except for network ID 324)
   - Fetch De.Fi reports for each token
   - Analyze and filter issues
   - Save individual reports in the `reports` folder
   - Generate a consolidated report in Markdown and CSV formats under the `output` folder

## Output

- Individual token reports are saved in the `reports` folder
- A consolidated Markdown report is generated at `output/report.md`
- A CSV summary is generated at `output/report.csv`

## Parsing the output report

The `output/report.md` file contains a structured report of issues found for each token. Here's how to interpret it:

1. The report is organized by blockchain networks (e.g., ethereum, polygon).
2. Under each network, you'll find sections for each analyzed token.
3. For each token, you'll see:
   - Token name
   - Contract address
   - Explorer URL
   - List of issue categories found
   - Detailed list of issues under each category

Use this report to quickly identify which tokens have issues and what types of issues they have. The explorer URL can be used to further investigate the token's contract on the blockchain explorer.

## Customization

- Modify `issueClassification.json` to update issue categories and classifications
