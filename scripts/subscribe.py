from brownie import Pyramid, accounts, Wei, config
from scripts.library import getAccount

FEE_AMOUNT = Wei(config[Contract][Parameters][Fee_Amount])
WAIT_TIME = config[Contract][Parameters][Wait_Time]


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
    print(f"Sent! Awaiting {WAIT_TIME} confirmations...")
    transaction.wait(WAIT_TIME)
    print("Confirmed!")