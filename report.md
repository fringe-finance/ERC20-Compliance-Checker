




# arbitrum



####  | L2ArbitrumToken
**Address:** 0x912CE59144191C1204E64559FE8253a0e49E6548

###### Issue Categories
- tokenVuln

###### tokenVuln Issues
- de.fi | The contract's owner can be changed by anyone.
- de.fi | Unprotected contract initializer, vulnerable to re-execution, immediate action needed for security.



####  | ArbFiatToken
**Address:** 0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8

###### Issue Categories
- adminSeizure
- tokenVuln

###### adminSeizure Issues
- de.fi | Token transfers can be paused, preventing swapping or selling.
- de.fi | Wallets can be blacklisted from being able to transfer, swap or sell this token.

###### tokenVuln Issues
- de.fi | The contract's owner can be changed by anyone.
- de.fi | Unprotected contract initializer, vulnerable to re-execution, immediate action needed for security.



####  | ArbitrumExtension
**Address:** 0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9

###### Issue Categories
- adminSeizure

###### adminSeizure Issues
- de.fi | Wallets can be blacklisted from being able to transfer, swap or sell this token.
- de.fi | Detected whitelisting feature enables unique users to bypass restrictions, potentially raising security and integrity concerns.



####  | GMX(GMX)
**Address:** 0xfc5A1A6EB076a2C7aD06eD22C90d7E710E35ad0a

###### Issue Categories
- adminSeizure

###### adminSeizure Issues
- de.fi | Detected whitelisting feature enables unique users to bypass restrictions, potentially raising security and integrity concerns.






# ethereum



####  | Uniswap (UNI) | Uni(Uniswap)
**Address:** 0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984

###### Issue Categories
- allowanceBugs
- balanceVariability
- theftOrInflation
- viewInaccuracies

###### allowanceBugs Issues
- ercx | Multiple `transferFrom` calls of positive amounts are NOT ALLOWED even though the sum of the transferred amounts is  less than or equal to the tokenSender's balance and approvals are given by the tokenSender.

###### balanceVariability Issues
- ercx | The `transfer` function TAKES fees at test execution time.
- ercx | The `transfer` function HAS the potential to take fees.
- ercx | The `transfer` function TAKES fees at test execution time.

###### theftOrInflation Issues
- ercx | Multiple calls of `transferFrom` ARE allowed even though the allowance has reached zero.

###### viewInaccuracies Issues
- ercx | A successful `balanceOf(account)` call does NOT return balance of `account` correctly after two dummy users' balances are initialized.



####  | Wrapped BTC (WBTC) | WBTC(Wrapped BTC)
**Address:** 0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599

###### Issue Categories
- adminSeizure

###### adminSeizure Issues
- de.fi | Token transfers can be paused, preventing swapping or selling.



####  | Frax Share (FXS) | FRAXShares(Frax Share)
**Address:** 0x3432B6A60D23Ca0dFCa7761B7ab56459D9C964D0

###### Issue Categories
- allowanceBugs
- balanceVariability
- theftOrInflation

###### allowanceBugs Issues
- ercx | Multiple `transfer` calls of positive amounts are NOT ALLOWED even though the sum of the transferred amounts is less than or equal to the tokenSender's balance.
- ercx | Multiple `transferFrom` calls of positive amounts are NOT ALLOWED even though the sum of the transferred amounts is  less than or equal to the tokenSender's balance and approvals are given by the tokenSender.
- ercx | A tokenReceiver CANNOT call `transferFrom` of the tokenSender's total balance amount even though tokenSender has approved that.

###### balanceVariability Issues
- ercx | The `transferFrom` function HAS the potential to take fees.
- ercx | The `transfer` function TAKES fees at test execution time.
- ercx | The `transfer` function HAS the potential to take fees.
- ercx | The `transfer` function TAKES fees at test execution time.
- ercx | A `msg.sender` CANNOT call `transfer` of her total balance amount to a tokenReceiver or the balances were not modified as expected.
- ercx | The contract's `totalSupply` variable IS altered after `transfer` is called.
- ercx | The contract's `totalSupply` variable IS altered after `transferFrom` is called.
- ercx | A successful call of `transfer` UPDATES the balance of users who are neither the tokenSender nor the tokenReceiver.
- ercx | A successful call of `transferFrom` UPDATES the balance of users who are neither the tokenSender nor the tokenReceiver.

###### theftOrInflation Issues
- ercx | Multiple calls of `transferFrom` ARE allowed even though the allowance has reached zero.



####  | Badger (BADGER) | MiniMeToken(Badger)
**Address:** 0x3472A5A71965499acd81997a54BBA8D852C6E53d

###### Issue Categories
- adminSeizure

###### adminSeizure Issues
- de.fi | Token transfers can be paused, preventing swapping or selling.
- de.fi | The contract owner is able to control all token holders' balances.



####  | Paxos Gold (PAXG) | PAXGImplementation
**Address:** 0x45804880De22913dAFE09f4980848ECE6EcbAf78

###### Issue Categories
- adminSeizure
- allowanceBugs
- balanceVariability

###### adminSeizure Issues
- de.fi | Token transfers can be paused, preventing swapping or selling.
- de.fi | Wallets can be blacklisted from being able to transfer, swap or sell this token.
- de.fi | The contract owner is able to control all token holders' balances.

###### allowanceBugs Issues
- ercx | A tokenReceiver CANNOT call `transferFrom` of the tokenSender's total balance amount even though tokenSender has approved that.

###### balanceVariability Issues
- ercx | The `transferFrom` function HAS the potential to take fees.
- ercx | The `transfer` function TAKES fees at test execution time.
- ercx | The `transfer` function HAS the potential to take fees.
- ercx | The `transfer` function TAKES fees at test execution time.
- ercx | Self `transfer` call of positive amount is NOT ALLOWED or it MODIFIED the balance.
- ercx | A `msg.sender` CANNOT call `transfer` of her total balance amount to a tokenReceiver or the balances were not modified as expected.



####  | Lido: LDO Token | MiniMeToken(Lido DAO Token)
**Address:** 0x5A98FcBEA516Cf06857215779Fd812CA3beF1B32

###### Issue Categories
- adminSeizure
- allowanceBugs
- balanceVariability
- theftOrInflation
- viewInaccuracies

###### adminSeizure Issues
- de.fi | Token transfers can be paused, preventing swapping or selling.
- de.fi | The contract owner is able to control all token holders' balances.

###### allowanceBugs Issues
- ercx | Multiple `transfer` calls of positive amounts are NOT ALLOWED even though the sum of the transferred amounts is less than or equal to the tokenSender's balance.
- ercx | Multiple `transferFrom` calls of positive amounts are NOT ALLOWED even though the sum of the transferred amounts is  less than or equal to the tokenSender's balance and approvals are given by the tokenSender.
- ercx | A tokenReceiver CANNOT call `transferFrom` of the tokenSender's total balance amount even though tokenSender has approved that.
- ercx | A tokenReceiver CANNOT call `transferFrom` of the tokenSender's total balance amount of zero.

###### balanceVariability Issues
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

###### theftOrInflation Issues
- ercx | Multiple calls of `transferFrom` ARE allowed even though the allowance has reached zero.

###### viewInaccuracies Issues
- ercx | A `msg.sender` CANNOT retrieve his/her own balance.
- ercx | A `msg.sender` CANNOT retrieve balance of an address different from his/hers.



####  | PepeToken(Pepe)
**Address:** 0x6982508145454Ce325dDbE47a25d4ec3d2311933

###### Issue Categories
- adminSeizure

###### adminSeizure Issues
- de.fi | Wallets can be blacklisted from being able to transfer, swap or sell this token.
- de.fi | The max/min amount of token transferred can be limited.



####  | SushiSwap: SUSHI Token | SushiToken(SushiToken)
**Address:** 0x6B3595068778DD592e39A122f4f5a5cF09C90fE2

###### Issue Categories
- allowanceBugs
- balanceVariability
- theftOrInflation
- viewInaccuracies

###### allowanceBugs Issues
- ercx | Multiple `transfer` calls of positive amounts are NOT ALLOWED even though the sum of the transferred amounts is less than or equal to the tokenSender's balance.
- ercx | Multiple `transferFrom` calls of positive amounts are NOT ALLOWED even though the sum of the transferred amounts is  less than or equal to the tokenSender's balance and approvals are given by the tokenSender.
- ercx | A tokenReceiver CANNOT call `transferFrom` of the tokenSender's total balance amount even though tokenSender has approved that.
- ercx | A tokenReceiver CANNOT call `transferFrom` of the tokenSender's total balance amount of zero.

###### balanceVariability Issues
- ercx | Test fee taking transfer [[[not found]]]
- ercx | Test fee taking transfer from [[[not found]]]
- ercx | Self `transfer` call of positive amount is NOT ALLOWED or it MODIFIED the balance.
- ercx | A `msg.sender` CANNOT call `transfer` of her total balance amount to a tokenReceiver or the balances were not modified as expected.
- ercx | The contract's `totalSupply` variable IS altered after `transfer` is called.
- ercx | The contract's `totalSupply` variable IS altered after `transferFrom` is called.
- ercx | A successful call of `transfer` UPDATES the balance of users who are neither the tokenSender nor the tokenReceiver.
- ercx | A successful call of `transferFrom` UPDATES the balance of users who are neither the tokenSender nor the tokenReceiver.
- ercx | Self `transfer` call of zero amount is NOT ALLOWED or it MODIFIES the balance.
- ercx | A `msg.sender` CANNOT call `transfer` of her total balance amount of zero to a tokenReceiver or the balances were modified.

###### theftOrInflation Issues
- ercx | Multiple calls of `transferFrom` ARE allowed even though the allowance has reached zero.

###### viewInaccuracies Issues
- ercx | A `msg.sender` CANNOT retrieve his/her own balance.
- ercx | A `msg.sender` CANNOT retrieve balance of an address different from his/hers.



####  | Polygon (Matic): Matic Token | MaticToken(Matic Token)
**Address:** 0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0

###### Issue Categories
- adminSeizure

###### adminSeizure Issues
- de.fi | Token transfers can be paused, preventing swapping or selling.



####  | Maker (MKR) | DSToken(Maker)
**Address:** 0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2

###### Issue Categories
- adminSeizure

###### adminSeizure Issues
- de.fi | Token transfers can be paused, preventing swapping or selling.



####  | USD Coin (USDC) | FiatTokenV2_1
**Address:** 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48

###### Issue Categories
- adminSeizure

###### adminSeizure Issues
- de.fi | Token transfers can be paused, preventing swapping or selling.
- de.fi | Wallets can be blacklisted from being able to transfer, swap or sell this token.



####  | Synthetix Network Token (SNX) | ProxyERC20(Synthetix Network Token)
**Address:** 0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F

###### Issue Categories
- allowanceBugs
- balanceVariability
- theftOrInflation
- viewInaccuracies

###### allowanceBugs Issues
- ercx | Multiple `transfer` calls of positive amounts are NOT ALLOWED even though the sum of the transferred amounts is less than or equal to the tokenSender's balance.
- ercx | Multiple `transferFrom` calls of positive amounts are NOT ALLOWED even though the sum of the transferred amounts is  less than or equal to the tokenSender's balance and approvals are given by the tokenSender.
- ercx | A tokenReceiver CANNOT call `transferFrom` of the tokenSender's total balance amount even though tokenSender has approved that.
- ercx | A tokenReceiver CANNOT call `transferFrom` of the tokenSender's total balance amount of zero.

###### balanceVariability Issues
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

###### theftOrInflation Issues
- ercx | Multiple calls of `transferFrom` ARE allowed even though the allowance has reached zero.

###### viewInaccuracies Issues
- ercx | A `msg.sender` CANNOT retrieve his/her own balance.
- ercx | A `msg.sender` CANNOT retrieve balance of an address different from his/hers.






# optimism



####  | OVMFiatToken(USD Coin)
**Address:** 0x7F5c764cBc14f9669B88837ca1490cCa17c31607

###### Issue Categories
- adminSeizure

###### adminSeizure Issues
- de.fi | Token transfers can be paused, preventing swapping or selling.
- de.fi | Wallets can be blacklisted from being able to transfer, swap or sell this token.






# polygon



####  | USD Coin (PoS) (USDC) | UChildAdministrableERC20
**Address:** 0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174

###### Issue Categories
- adminSeizure

###### adminSeizure Issues
- de.fi | Token transfers can be paused, preventing swapping or selling.
- de.fi | Wallets can be blacklisted from being able to transfer, swap or sell this token.






# zksync

