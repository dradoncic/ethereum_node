from web3 import Web3
from pprint import pprint

ARCHIVE_NODE_RPC = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ARCHIVE_NODE_RPC))


def get_eth_balance(address, block="latest"):
    try:
        return web3.eth.get_balance(address, block)
    except Exception as e:
        print(f"[ERROR] Could not fetch balance: {e}")
        return None

def print_eth_balance(address, block="latest"):
    balance = get_eth_balance(address, block)
    if balance is not None:
        print(f"[BALANCE] {address} at block {block}: {Web3.from_wei(balance, 'ether')} ETH")
    else:
        print("Invalid Query")

def get_block_transaction(block):
    try:
        return web3.eth.get_block(block, full_transactions=True)
    except Exception as e:
        print(f"[ERROR] Could not fetch block transactions: {e}")
        return None

def print_block_transaction(block):
    block_data = get_block_transaction(block)
    if block_data:
        print(f"\n[BLOCK {block} TRANSACTIONS:")
        for tx in block_data['transactions']:
            pprint({
                "hash": tx.hash.hex(),
                "from": tx["from"],
                "to": tx["to"],
                "value": Web3.from_wei(tx["value"], "ether"),
                "gas": tx["gas"],
                "gas_price": Web3.from_wei(tx["gasPrice"], "gwei"),
                "nonce": tx["nonce"]
            })
    else:
        print("Invalid Query")


if __name__ == '__main__':
    block = 21990443

    print_block_transaction(block)

