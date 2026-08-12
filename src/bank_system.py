from . import file_handler
from .account import Account
from datetime import datetime
class BankSystem:
    def account_exists(self, account_number):
        return file_handler.account_file_exists(account_number)
    def load_account(self, account_number):
        content = file_handler.read_account_file(account_number)
        profile = content.split("TRANSACTIONS:", 1)[0].strip()
        return Account.from_line(profile)
    
    def save_account(self, account):
        account_number = account._account_number
        if file_handler.account_file_exists(account_number):
            content = file_handler.read_account_file(account_number)
            parts = content.split("TRANSACTIONS:", 1)
            transactions = parts[1].strip() if len(parts) > 1 else ""
            if transactions:
                content = account.to_line() + "\nTRANSACTIONS:\n" + transactions + "\n"
            else:
                content = account.to_line() + "\nTRANSACTIONS:\n"
        else:
            content = account.to_line() + "\nTRANSACTIONS:\n"
        file_handler.write_account_file(account_number, content)

    def deposit(self, account, amount):
        account.deposit(amount)
        self.save_account(account)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = f"{timestamp},DEPOSIT,{amount},{account._balance}"
        file_handler.append_transaction_line(account._account_number, transaction)

    def withdraw(self, account, amount):
        account.withdraw(amount)
        self.save_account(account)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = f"{timestamp},WITHDRAW,{amount},{account._balance}"
        file_handler.append_transaction_line(account._account_number, transaction)

    def get_transaction_history(self, account_number):
        content = file_handler.read_account_file(account_number)
        parts = content.split("TRANSACTIONS:", 1)
        if len(parts) < 2:
            return []
        transactions = parts[1].strip()
        if not transactions:
            return []
        return transactions.splitlines()
    

    def transfer(self, sender, receiver_account_number, amount):
        if not self.account_exists(receiver_account_number):
            raise ValueError("Receiver account does not exist")

        if sender._account_number == receiver_account_number:
            raise ValueError("Cannot transfer to the same account")

        if amount <= 0:
            raise ValueError("Please enter a valid amount")

        receiver = self.load_account(receiver_account_number)

        if not sender.can_withdraw(amount):
            raise ValueError("You don't have enough balance to transfer")

        sender.withdraw(amount)
        receiver.deposit(amount)

        self.save_account(sender)
        self.save_account(receiver)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        sender_transaction = (
            f"{timestamp},TRANSFER_OUT,{amount},{sender._balance}"
        )

        receiver_transaction = (
            f"{timestamp},TRANSFER_IN,{amount},{receiver._balance}"
        )

        file_handler.append_transaction_line(
            sender._account_number,
            sender_transaction
        )

        file_handler.append_transaction_line(
            receiver._account_number,
            receiver_transaction
        )

