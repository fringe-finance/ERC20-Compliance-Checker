




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






# optimism






# polygon






# zksync

