from brownie import network, accounts

def getAccount():
    print("Enter your address private key (for signing, not distributed or saved):")
    account = accounts.add(input())
    return account