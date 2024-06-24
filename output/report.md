




# arbitrum






# ethereum



### Uniswap
**Address:** 0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984
**Explorer url:** https://etherscan.io/address/0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984#code

##### Issue Categories
###### active transfer constraints
###### view inaccuracies

##### active transfer constraints Issues
- ercx | Multiple `transfer` calls of positive amounts are NOT ALLOWED even though the sum of the transferred amounts is less than or equal to the tokenSender's balance. | testPositiveMultipleTransfer

##### view inaccuracies Issues
- ercx | A successful `balanceOf(account)` call does NOT return balance of `account` correctly after two dummy users' balances are initialized. | testUserBalanceInitialized



### Frax Share
**Address:** 0x3432B6A60D23Ca0dFCa7761B7ab56459D9C964D0
**Explorer url:** https://etherscan.io/address/0x3432B6A60D23Ca0dFCa7761B7ab56459D9C964D0#code

##### Issue Categories
###### active transfer constraints

##### active transfer constraints Issues
- ercx | Multiple `transfer` calls of positive amounts are NOT ALLOWED even though the sum of the transferred amounts is less than or equal to the tokenSender's balance. | testPositiveMultipleTransfer
- ercx | A `msg.sender` CANNOT call `transfer` of her total balance amount to a tokenReceiver or the balances were not modified as expected. | testPositiveTotalTransferToOther



### Pepe
**Address:** 0x6982508145454Ce325dDbE47a25d4ec3d2311933
**Explorer url:** https://etherscan.io/address/0x6982508145454Ce325dDbE47a25d4ec3d2311933#code

##### Issue Categories
###### active transfer constraints

##### active transfer constraints Issues
- de.fi | The max/min amount of token transferred can be limited. | 211



### Tether USD
**Address:** 0xdAC17F958D2ee523a2206206994597C13D831ec7
**Explorer url:** https://etherscan.io/address/0xdAC17F958D2ee523a2206206994597C13D831ec7#code

##### Issue Categories
###### active transfer constraints
###### balance variability

##### active transfer constraints Issues
- de.fi | The max/min amount of token transferred can be limited. | 211

##### balance variability Issues
- ercx | The `transferFrom` function HAS the potential to take fees. | testFeeTakingTransferFromPotential
- ercx | The `transfer` function HAS the potential to take fees. | testFeeTakingTransferPotential



### Ondo
**Address:** 0xfAbA6f8e4a5E8Ab82F62fe7C39859FA577269BE3
**Explorer url:** https://etherscan.io/address/0xfAbA6f8e4a5E8Ab82F62fe7C39859FA577269BE3#code

##### Issue Categories
###### active transfer constraints
###### balance variability
###### theft or inflation
###### view inaccuracies

##### active transfer constraints Issues
- ercx | Multiple `transfer` calls of positive amounts are NOT ALLOWED even though the sum of the transferred amounts is less than or equal to the tokenSender's balance. | testPositiveMultipleTransfer
- ercx | A `msg.sender` CANNOT call `transfer` of her total balance amount to a tokenReceiver or the balances were not modified as expected. | testPositiveTotalTransferToOther

##### balance variability Issues
- ercx | There is an issue when dealing the intended amount of tokens to dummy users for interacting with the contract. This could be due to issues with  (a) calling of the `transfer` function by the top token holder, or  (b) the presence of fees from the `transfer` function. | testDealIntendedTokensToDummyUsers
- ercx | The `transferFrom` function HAS the potential to take fees. | testFeeTakingTransferFromPotential
- ercx | The `transfer` function TAKES fees at test execution time. | testFeeTakingTransferFromPresent
- ercx | The `transfer` function HAS the potential to take fees. | testFeeTakingTransferPotential
- ercx | The `transfer` function TAKES fees at test execution time. | testFeeTakingTransferPresent
- ercx | Self `transfer` call of positive amount is NOT ALLOWED or it MODIFIED the balance. | testPositiveSelfTransfer
- ercx | The contract's `totalSupply` variable IS altered after `transfer` is called. | testTotalSupplyConstantAfterTransfer
- ercx | The contract's `totalSupply` variable IS altered after `transferFrom` is called. | testTotalSupplyConstantAfterTransferFrom
- ercx | A successful call of `transfer` UPDATES the balance of users who are neither the tokenSender nor the tokenReceiver. | testTransferDoesNotUpdateOthersBalances
- ercx | A successful call of `transferFrom` UPDATES the balance of users who are neither the tokenSender nor the tokenReceiver. | testTransferFromDoesNotUpdateOthersBalances

##### theft or inflation Issues
- ercx | A tokenReceiver CAN call `transferFrom` of an amount more than her allowance from the tokenSender. | testCannotTransferFromMoreThanAllowanceLowerThanBalance
- ercx | A tokenReceiver CAN call `transferFrom` of an amount more than the tokenSender's balance. | testCannotTransferFromMoreThanBalanceButLowerThanAllowance
- ercx | A tokenSender (which is also the `msg.sender`) CAN call `transfer` of an amount more than his balance.  | testCannotTransferMoreThanBalance
- ercx | A tokenReceiver CAN be able to call `transferFrom` of a positive amount from an tokenSender even though the tokenSender did not approve the tokenReceiver previously. | testNoApprovalCannotTransferFrom
- ercx | A successful `transferFrom` call of zero amount by any user other than the tokenSender, from and to different accounts, is NOT possible. | testZeroTransferFromByOtherPossibleFromAndToDifferentAccounts

##### view inaccuracies Issues
- ercx | A `msg.sender` CANNOT retrieve his/her own balance. | testBalanceOfCaller
- ercx | A `msg.sender` CANNOT retrieve balance of an address different from his/hers. | testBalanceOfNonCaller






# optimism






# polygon



### QuickSwap
**Address:** 0xB5C064F955D8e7F38fE0460C556a72987494eE17
**Explorer url:** https://polygonscan.com/address/0xB5C064F955D8e7F38fE0460C556a72987494eE17#code

##### Issue Categories
###### theft or inflation

##### theft or inflation Issues
- ercx | A tokenReceiver CAN call `transferFrom` of an amount more than the tokenSender's balance. | testCannotTransferFromMoreThanBalanceButLowerThanAllowance






# zksync

