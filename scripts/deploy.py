from brownie import accounts, config, Pyramid, network
from scripts.library import getAccount
from brownie.network.gas.strategies import GasNowStrategy
from brownie.network import gas_price

GAS_STRATEGY = 'standard'

def main():
    deploy_pyramid()

def deploy_pyramid():
    account = getAccount()
    gas_price(GasNowStrategy(GAS_STRATEGY))
    print(f"Gas strategy is: {GAS_STRATEGY}")
    print("Deploying...")
    my_pyramid = Pyramid.deploy({"from": account}, publish_source=True)
    print(f"Contract deployed to: {my_pyramid}")
