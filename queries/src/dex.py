import json
from web3 import Web3
from pprint import pprint

# Connect to Local Ethereum Node
WEB3_RPC = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(WEB3_RPC))

# Load Uniswap V3 ABI from abi.json
with open("abi.json", "r") as abi_file:
    ABI = json.load(abi_file)

# Uniswap V3 Pool Contract Address (Replace with the correct one)
POOL_ADDRESS = "0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640"  # Example: WETH/USDC

# Initialize contract
pool_contract = web3.eth.contract(address=POOL_ADDRESS, abi=ABI)

# Fetch the liquidity of the pool
def get_pool_liquidity():
    try:
        liquidity = pool_contract.functions.liquidity().call()
        print(f"[LIQUIDITY] Pool Liquidity: {liquidity}")
    except Exception as e:
        print(f"[ERROR] Failed to fetch liquidity: {e}")

# Fetch the current fee tier of the pool
def get_pool_fee():
    try:
        fee = pool_contract.functions.fee().call()
        print(f"[FEE] Uniswap V3 Pool Fee: {fee / 1e6:.2f}%")  # Convert to percentage
    except Excepton as e:
        print(f"[ERROR] Failed to fetch fee: {e}")

# Fetch reserves and price data
def get_pool_reserves():
    try:
        slot0 = pool_contract.functions.slot0().call()
        sqrt_price_x96 = slot0[0]  # sqrtPriceX96
        tick = slot0[1]  # Tick value

        print(f"[POOL DATA] sqrtPriceX96: {sqrt_price_x96}, Tick: {tick}")
    except Exception as e:
        print(f"[ERROR] Failed to fetch pool reserves: {e}")

# Fetch all swap events in a given block
def get_swaps(block):
    try:
        # Corrected event signature hash with 0x prefix
        swap_event_signature = web3.keccak(text="Swap(address,address,int256,int256,uint160,uint128,int24)").hex()
        
        logs = web3.eth.get_logs({
            "fromBlock": block,
            "toBlock": block,
            "address": POOL_ADDRESS,
            "topics": [swap_event_signature]
        })

        if not logs:
            print(f"[INFO] No swaps found in block {block}")
            return

        swaps = []
        for log in logs:
            decoded = web3.codec.decode(['int256', 'int256', 'uint160', 'uint128', 'int24'], log['data'])
            swaps.append({
                "amount0": decoded[0],
                "amount1": decoded[1],
                "sqrtPriceX96": decoded[2],
                "liquidity": decoded[3],
                "tick": decoded[4]
            })

        print(f"\n[SWAPS] Transactions at block {block}:")
        pprint(swaps)
    except Exception as e:
        print(f"[ERROR] Failed to fetch swap events: {e}")

# Run queries
if __name__ == "__main__":
    block_number = 18000000  # Replace with the block you want to analyze

    get_pool_liquidity()
    get_pool_fee()
    get_pool_reserves()
    get_swaps(block_number)

