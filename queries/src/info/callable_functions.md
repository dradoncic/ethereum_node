# Uniswap V3 -- View/Pure Functions

factory - Returns factory address

fee - Returns pool fee percentage (e.g., 3000 = 0.3%)

feeGrowthGlobal0X128 - Global fee growth for token0 (WETH)

feeGrowthGlobal1X128 - Global fee growth for token1 (USDC)

liquidity - Total active liquidity in pool

maxLiquidityPerTick - Max liquidity per tick

observations - Get oracle observation data by index

observe - Get cumulative tick/liquidity values

positions - Get position data by key

protocolFees - Get accumulated protocol fees

slot0 - Core pool state (sqrtPriceX96, tick, oracle data)

snapshotCumulativesInside - Get oracle data for a tick range

tickBitmap - Get tick bitmap data

tickSpacing - Get pool's tick spacing

ticks - Get tick data

token0 - Returns WETH address

token1 - Returns USDC address
