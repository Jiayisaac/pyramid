from brownie import network, accounts

def getAccount():
    if network.show_active() == "rinkeby":
        account = accounts.load("Rinkeby_Test1")
    else:
        account = accounts[0]
    return account