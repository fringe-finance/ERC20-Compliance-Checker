




# arbitrum



### Arbitrum
**Address:** 0x912CE59144191C1204E64559FE8253a0e49E6548
**Explorer url:** https://arbiscan.io/address/0x912CE59144191C1204E64559FE8253a0e49E6548#code

##### Issue Categories
###### token vuln

###### token vuln Issues
- de.fi | The contract's owner can be changed by anyone.
- de.fi | Unprotected contract initializer, vulnerable to re-execution, immediate action needed for security.



### USD Coin (Arb1)
**Address:** 0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8
**Explorer url:** https://arbiscan.io/address/0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8#code

##### Issue Categories
###### potential granular transfer constraints
###### token vuln

###### potential granular transfer constraints Issues
- de.fi | Wallets can be blacklisted from being able to transfer, swap or sell this token.

###### token vuln Issues
- de.fi | The contract's owner can be changed by anyone.
- de.fi | Unprotected contract initializer, vulnerable to re-execution, immediate action needed for security.



### Tether USD
**Address:** 0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9
**Explorer url:** https://arbiscan.io/address/0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9#code

##### Issue Categories
###### potential granular transfer constraints

###### potential granular transfer constraints Issues
- de.fi | Wallets can be blacklisted from being able to transfer, swap or sell this token.
- de.fi | Detected whitelisting feature enables unique users to bypass restrictions, potentially raising security and integrity concerns.



### GMX
**Address:** 0xfc5A1A6EB076a2C7aD06eD22C90d7E710E35ad0a
**Explorer url:** https://arbiscan.io/address/0xfc5A1A6EB076a2C7aD06eD22C90d7E710E35ad0a#code

##### Issue Categories
###### potential granular transfer constraints

###### potential granular transfer constraints Issues
- de.fi | Detected whitelisting feature enables unique users to bypass restrictions, potentially raising security and integrity concerns.






# ethereum



### Uniswap
**Address:** 0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984
**Explorer url:** https://etherscan.io/address/0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984#code

##### Issue Categories
###### active transfer constraints
###### view inaccuracies

###### active transfer constraints Issues
- ercx | Multiple `transfer` calls of positive amounts are NOT ALLOWED even though the sum of the transferred amounts is less than or equal to the tokenSender's balance.

###### view inaccuracies Issues
- ercx | A successful `balanceOf(account)` call does NOT return balance of `account` correctly after two dummy users' balances are initialized.



### Frax Share
**Address:** 0x3432B6A60D23Ca0dFCa7761B7ab56459D9C964D0
**Explorer url:** https://etherscan.io/address/0x3432B6A60D23Ca0dFCa7761B7ab56459D9C964D0#code

##### Issue Categories
###### active transfer constraints
###### balance variability

###### active transfer constraints Issues
- ercx | Multiple `transfer` calls of positive amounts are NOT ALLOWED even though the sum of the transferred amounts is less than or equal to the tokenSender's balance.

###### balance variability Issues
- ercx | A `msg.sender` CANNOT call `transfer` of her total balance amount to a tokenReceiver or the balances were not modified as expected.



### Badger
**Address:** 0x3472A5A71965499acd81997a54BBA8D852C6E53d
**Explorer url:** https://etherscan.io/address/0x3472A5A71965499acd81997a54BBA8D852C6E53d#code

##### Issue Categories
###### active transfer constraints
###### balance variability
###### potential granular transfer constraints
###### theft or inflation
###### view inaccuracies

###### active transfer constraints Issues
- ercx | Multiple `transfer` calls of positive amounts are NOT ALLOWED even though the sum of the transferred amounts is less than or equal to the tokenSender's balance.

###### balance variability Issues
- ercx | The `transferFrom` function HAS the potential to take fees.
- ercx | The `transfer` function TAKES fees at test execution time.
- ercx | The `transfer` function HAS the potential to take fees.
- ercx | The `transfer` function TAKES fees at test execution time.
- ercx | Self `transfer` call of positive amount is NOT ALLOWED or it MODIFIED the balance.
- ercx | A `msg.sender` CANNOT call `transfer` of her total balance amount to a tokenReceiver or the balances were not modified as expected.
- ercx | The contract's `totalSupply` variable IS altered after `transfer` is called.
- ercx | The contract's `totalSupply` variable IS altered after `transferFrom` is called.
- ercx | A successful call of `transfer` UPDATES the balance of users who are neither the tokenSender nor the tokenReceiver.
- ercx | A successful call of `transferFrom` UPDATES the balance of users who are neither the tokenSender nor the tokenReceiver.
- ercx | Self `transfer` call of zero amount is NOT ALLOWED or it MODIFIES the balance.
- ercx | A `msg.sender` CANNOT call `transfer` of her total balance amount of zero to a tokenReceiver or the balances were modified.

###### potential granular transfer constraints Issues
- de.fi | The contract owner is able to control all token holders' balances.

###### theft or inflation Issues
- ercx | Multiple calls of `transferFrom` ARE allowed even though the allowance has reached zero.

###### view inaccuracies Issues
- ercx | A `msg.sender` CANNOT retrieve his/her own balance.
- ercx | A `msg.sender` CANNOT retrieve balance of an address different from his/hers.



### Paxos Gold
**Address:** 0x45804880De22913dAFE09f4980848ECE6EcbAf78
**Explorer url:** https://etherscan.io/address/0x45804880De22913dAFE09f4980848ECE6EcbAf78#code

##### Issue Categories
###### balance variability
###### potential granular transfer constraints

###### balance variability Issues
- ercx | The `transferFrom` function HAS the potential to take fees.
- ercx | The `transfer` function TAKES fees at test execution time.
- ercx | The `transfer` function HAS the potential to take fees.
- ercx | The `transfer` function TAKES fees at test execution time.
- ercx | Self `transfer` call of positive amount is NOT ALLOWED or it MODIFIED the balance.
- ercx | A `msg.sender` CANNOT call `transfer` of her total balance amount to a tokenReceiver or the balances were not modified as expected.

###### potential granular transfer constraints Issues
- de.fi | Wallets can be blacklisted from being able to transfer, swap or sell this token.
- de.fi | The contract owner is able to control all token holders' balances.



### Wootrade Network
**Address:** 0x4691937a7508860F876c9c0a2a617E7d9E945D4B
**Explorer url:** https://etherscan.io/address/0x4691937a7508860F876c9c0a2a617E7d9E945D4B#code

##### Issue Categories
###### balance variability

###### balance variability Issues
- ercx | Self `transfer` call of zero amount is NOT ALLOWED or it MODIFIES the balance.
- ercx | A `msg.sender` CANNOT call `transfer` of her total balance amount of zero to a tokenReceiver or the balances were modified.



### Lido DAO Token
**Address:** 0x5A98FcBEA516Cf06857215779Fd812CA3beF1B32
**Explorer url:** https://etherscan.io/address/0x5A98FcBEA516Cf06857215779Fd812CA3beF1B32#code

##### Issue Categories
###### potential granular transfer constraints

###### potential granular transfer constraints Issues
- de.fi | The contract owner is able to control all token holders' balances.



### Pepe
**Address:** 0x6982508145454Ce325dDbE47a25d4ec3d2311933
**Explorer url:** https://etherscan.io/address/0x6982508145454Ce325dDbE47a25d4ec3d2311933#code

##### Issue Categories
###### active transfer constraints
###### potential granular transfer constraints

###### active transfer constraints Issues
- de.fi | The max/min amount of token transferred can be limited.

###### potential granular transfer constraints Issues
- de.fi | Wallets can be blacklisted from being able to transfer, swap or sell this token.



### USD Coin
**Address:** 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48
**Explorer url:** https://etherscan.io/address/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48#code

##### Issue Categories
###### potential granular transfer constraints

###### potential granular transfer constraints Issues
- de.fi | Wallets can be blacklisted from being able to transfer, swap or sell this token.



### Synthetix Network Token
**Address:** 0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F
**Explorer url:** https://etherscan.io/address/0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F#code

##### Issue Categories
###### active transfer constraints
###### balance variability
###### theft or inflation
###### view inaccuracies

###### active transfer constraints Issues
- ercx | Multiple `transfer` calls of positive amounts are NOT ALLOWED even though the sum of the transferred amounts is less than or equal to the tokenSender's balance.

###### balance variability Issues
- ercx | The `transferFrom` function HAS the potential to take fees.
- ercx | The `transfer` function TAKES fees at test execution time.
- ercx | The `transfer` function HAS the potential to take fees.
- ercx | The `transfer` function TAKES fees at test execution time.
- ercx | Self `transfer` call of positive amount is NOT ALLOWED or it MODIFIED the balance.
- ercx | A `msg.sender` CANNOT call `transfer` of her total balance amount to a tokenReceiver or the balances were not modified as expected.
- ercx | The contract's `totalSupply` variable IS altered after `transfer` is called.
- ercx | The contract's `totalSupply` variable IS altered after `transferFrom` is called.
- ercx | A successful call of `transfer` UPDATES the balance of users who are neither the tokenSender nor the tokenReceiver.
- ercx | A successful call of `transferFrom` UPDATES the balance of users who are neither the tokenSender nor the tokenReceiver.
- ercx | Self `transfer` call of zero amount is NOT ALLOWED or it MODIFIES the balance.
- ercx | A `msg.sender` CANNOT call `transfer` of her total balance amount of zero to a tokenReceiver or the balances were modified.

###### theft or inflation Issues
- ercx | A tokenReceiver CAN call `transferFrom` of an amount more than her allowance from the tokenSender.
- ercx | A tokenReceiver CAN call `transferFrom` of an amount more than the tokenSender's balance.
- ercx | A tokenSender (which is also the `msg.sender`) CAN call `transfer` of an amount more than his balance. 
- ercx | A tokenReceiver CAN be able to call `transferFrom` of a positive amount from an tokenSender even though the tokenSender did not approve the tokenReceiver previously.

###### view inaccuracies Issues
- ercx | A successful `balanceOf(account)` call does NOT return balance of `account` correctly after two dummy users' balances are initialized.






# optimism



### USD Coin
**Address:** 0x7F5c764cBc14f9669B88837ca1490cCa17c31607
**Explorer url:** https://optimistic.etherscan.io/address/0x7F5c764cBc14f9669B88837ca1490cCa17c31607#code

##### Issue Categories
###### potential granular transfer constraints

###### potential granular transfer constraints Issues
- de.fi | Wallets can be blacklisted from being able to transfer, swap or sell this token.






# polygon



### USD Coin (PoS)
**Address:** 0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174
**Explorer url:** https://polygonscan.com/address/0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174#code

##### Issue Categories
###### potential granular transfer constraints

###### potential granular transfer constraints Issues
- de.fi | Wallets can be blacklisted from being able to transfer, swap or sell this token.






# zksync
