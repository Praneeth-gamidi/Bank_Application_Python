import random
from .account import Account
from .bank_system import BankSystem
def register(bank, name, pin, initial_balance=0.0):
    while True:
        account_number = str(random.randint(1000000000, 9999999999))
        if not bank.account_exists(account_number):
            break
    account = Account(account_number, name, pin, initial_balance)
    bank.save_account(account)
    return account_number


def login(bank, account_number, pin):
    if not bank.account_exists(account_number):
        raise ValueError("Invalid account number or PIN")

    account = bank.load_account(account_number)

    if not account.verify_pin(pin):
        raise ValueError("Invalid account number or PIN")

    return account

