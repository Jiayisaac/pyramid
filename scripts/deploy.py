from brownie import accounts, config, Pyramid, network
from scripts.library import getAccount

def main():
    deploy_pyramid()

def deploy_pyramid():
    account = getAccount()
    print("Deploying...")
    if network.show_active() == "rinkeby":
        my_pyramid = Pyramid.deploy({"from": account}, publish_source=True)
    else:
        my_pyramid = Pyramid.deploy({"from": account})

    print(f"Contract deployed to: {my_pyramid}")
