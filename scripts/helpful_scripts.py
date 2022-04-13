from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

from distutils.command.config import config

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000

PRIVATE_KEY = 0Xfdd285a6e2faa55b2d89827c1bed33481b25cd93461f0a0beadcf5179d63275c

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(PRIVATE_KEY)
        # return PRIVATE_KEY

def deploy_mocks():
     print(f"The active network is {network.show_active()}")
        print(f"Deploying Mocks...")
        if len(MockV3Aggregator) <= 0:
            MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE,"ether"), {"from":get_account()})
        print("Mocks Deployed!!!")