from .account import Account
from .auth_service import login, register
from .bank_system import BankSystem


class CLI:
    def __init__(self, bank: BankSystem):
        self.bank = bank

    def run(self) -> None:
        while True:
            print("\n===== BANKING APPLICATION =====")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.register_user()
            elif choice == "2":
                self.login_user()
            elif choice == "3":
                print("Thank you for using the Banking Application.")
                break
            else:
                print("Invalid choice. Please try again.")

    def register_user(self) -> None:
        name = input("Enter your name: ")
        pin = input("Enter your PIN: ")
        balance_input = input("Enter initial balance: ")

        try:
            initial_balance = float(balance_input)
            account_number = register(
                self.bank,
                name,
                pin,
                initial_balance
            )
            print(f"Account created successfully.")
            print(f"Your account number is: {account_number}")
        except ValueError as e:
            print(f"Registration failed: {e}")

    def login_user(self) -> None:
        account_number = input("Enter account number: ")
        pin = input("Enter PIN: ")

        try:
            account = login(self.bank, account_number, pin)
            print(f"Welcome, {account._name}!")
            self.account_menu(account)
        except ValueError as e:
            print(f"Login failed: {e}")

    def account_menu(self, account: Account) -> None:
        while True:
            print("\n===== ACCOUNT MENU =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Transaction History")
            print("6. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.show_balance(account)
            elif choice == "2":
                self.deposit(account)
            elif choice == "3":
                self.withdraw(account)
            elif choice == "4":
                self.transfer(account)
            elif choice == "5":
                self.show_transaction_history(account)
            elif choice == "6":
                print("Logged out successfully.")
                break
            else:
                print("Invalid choice. Please try again.")

    def show_balance(self, account: Account) -> None:
        print(f"Current balance: {account._balance}")

    def deposit(self, account: Account) -> None:
        try:
            amount = float(input("Enter deposit amount: "))
            self.bank.deposit(account, amount)
            print(f"Deposit successful. New balance: {account._balance}")
        except ValueError as e:
            print(f"Deposit failed: {e}")

    def withdraw(self, account: Account) -> None:
        try:
            amount = float(input("Enter withdrawal amount: "))
            self.bank.withdraw(account, amount)
            print(f"Withdrawal successful. New balance: {account._balance}")
        except ValueError as e:
            print(f"Withdrawal failed: {e}")

    def transfer(self, account: Account) -> None:
        receiver = input("Enter receiver account number: ")

        try:
            amount = float(input("Enter transfer amount: "))
            self.bank.transfer(account, receiver, amount)
            print(f"Transfer successful. New balance: {account._balance}")
        except ValueError as e:
            print(f"Transfer failed: {e}")

    def show_transaction_history(self, account: Account) -> None:
        try:
            history = self.bank.get_transaction_history(
                account._account_number
            )

            print("\n===== TRANSACTION HISTORY =====")

            if not history:
                print("No transactions found.")
                return

            for transaction in history:
                print(transaction)

        except FileNotFoundError as e:
            print(f"Unable to retrieve transaction history: {e}")


if __name__ == "__main__":
    bank = BankSystem()
    cli = CLI(bank)
    cli.run()