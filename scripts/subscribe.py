from brownie import Pyramid, accounts, config
from scripts.deploy import GAS_STRATEGY
from scripts.library import getAccount
from brownie.network.gas.strategies import GasNowStrategy
from brownie.network import gas_price
from web3 import Web3

def main():
    pyramid_subscribe()

def pyramid_subscribe():
    my_pyramid = Pyramid[-1]
    GAS_STRATEGY = "standard"
    print("Please input your referrers account, or leave blank to select a random member")
    Referrer_address = input()
    print("Please input your account private key (this is only used to sign the transaction, is not saved and transmitted to the network) starting with 0x")
    Account = accounts.add(input())
    print(f"Your account is: {Account}")
    print("Sending transaction...")
    gas_price(GasNowStrategy(GAS_STRATEGY))
    print(f"Gas strategy is: {GAS_STRATEGY}")
    txn_parameters = {
        "from": Account,
        "amount": Web3.toWei(0.05, "ether")
    }
    if len(Referrer_address)==0:
        print("Random member address selected")
        transaction = my_pyramid.subscribeToRandomAddress(txn_parameters)
    else:
        transaction = my_pyramid.subscribe(Referrer_address, txn_parameters)
    print("Sent! Awaiting 3 confirmations...")
    transaction.wait(3)
    print("Confirmed!")