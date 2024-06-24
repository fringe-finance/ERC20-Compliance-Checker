




# arbitrum



### VelaToken
**Address:** 0x088cd8f5ef3652623c22d48b1605dcfe860cd704
**Explorer url:** https://arbiscan.io/address/0x088cd8f5ef3652623c22d48b1605dcfe860cd704#code

##### Issue Categories
###### undetermined

##### undetermined Issues
- ercx | The contract owner can control balance by minting numerous tokens to an account (via `mint(address,uint256)` or `mintToken(address,uint256)` or `issue(address,uint256)`),  overflowing its balance to a small figure. | testBalanceDoesNotOverflowByMinting
- ercx | It was possible to mint tokens (via `mint(address,uint256)` or `mintToken(address,uint256)` or `issue(address,uint256)`) to the zero address. | testMintingToZeroAddressShouldFail
- ercx | After minting some token (via `mint(address,uint256)` or `mintToken(address,uint256)` or `issue(address,uint256)`), the user balance was not updated correctly. | testMintingUpdatesBalance
- ercx | After minting some token (via `mint(address,uint256)` or `mintToken(address,uint256)` or `issue(address,uint256)`), the total supply was not updated correctly. | testMintingUpdatesTotalSupply
- ercx | By minting zero token (via `mint(address,uint256)` or `mintToken(address,uint256)` or `issue(address,uint256)`), the balance of the target address changed. | testMintingZeroShouldNotChangeBalance
- ercx | By minting zero token (via `mint(address,uint256)` or `mintToken(address,uint256)` or `issue(address,uint256)`), the total supply changed. | testMintingZeroShouldNotChangeTotalSupply
- ercx | The contract owner can bring about an overflow and issue random amounts of tokens (via `mint(address,uint256)` or `mintToken(address,uint256)` or `issue(address,uint256)`)  by passing a great value and pass the check of max minting value. | testNoExcessByMintingViaOverflow
- ercx | An overflow happened with variable totalSupply when the sum of tokens changed via minting (via `mint(address,uint256)` or `mintToken(address,uint256)` or `issue(address,uint256)`). | testTotalSupplyDoesNotOverflowByMinting






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



### Ondo
**Address:** 0xfAbA6f8e4a5E8Ab82F62fe7C39859FA577269BE3
**Explorer url:** https://etherscan.io/address/0xfAbA6f8e4a5E8Ab82F62fe7C39859FA577269BE3#code

##### Issue Categories
###### active transfer constraints
###### balance variability
###### theft or inflation
###### undetermined
###### view inaccuracies

##### active transfer constraints Issues
- ercx | Multiple `transfer` calls of positive amounts are NOT ALLOWED even though the sum of the transferred amounts is less than or equal to the tokenSender's balance. | testPositiveMultipleTransfer
- ercx | A `msg.sender` CANNOT call `transfer` of her total balance amount to a tokenReceiver or the balances were not modified as expected. | testPositiveTotalTransferToOther

##### balance variability Issues
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

##### undetermined Issues
- ercx | A successful `transferFrom` call of zero amount by any user other than the tokenSender, from and to the same account, is NOT possible. | testZeroTransferFromByOtherFromAndToSameAccountPossible
- ercx | A successful `transferFrom` call of zero amount by any user other than the tokenSender, from and to different accounts, is NOT possible. | testZeroTransferFromByOtherPossibleFromAndToDifferentAccounts

##### view inaccuracies Issues
- ercx | A `msg.sender` CANNOT retrieve his/her own balance. | testBalanceOfCaller
- ercx | A `msg.sender` CANNOT retrieve balance of an address different from his/hers. | testBalanceOfNonCaller






# optimism






# polygon






# zksync

