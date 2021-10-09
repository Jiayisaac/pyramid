from brownie import Pyramid, accounts, Wei
from scripts.library import getAccount

FEE_AMOUNT = Wei("0.05 ether")

def main():
    pyramid_subscribe()

def pyramid_subscribe():
    my_pyramid = Pyramid[-1]
    print("Please input your referrers account, or leave blank to select a random member")
    Referrer_address = input()
    print("Please input your account private key, starting with 0x")
    Account = accounts.add(input())
    print(f"Your account is: {Account}")
    print("Sending transaction...")
    txn_parameters = {
        "from": Account,
        "amount": FEE_AMOUNT
    }
    if len(Referrer_address)==0:
        print("Random member address selected")
        transaction = my_pyramid.subscribeToRandomAddress(txn_parameters)
    else:
        transaction = my_pyramid.subscribe(Referrer_address, txn_parameters)
    print("Sent! Awaiting 3 confirmations...")
    transaction.wait(3)
    print("Confirmed!")