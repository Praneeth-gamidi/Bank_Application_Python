from src.bank_system import BankSystem
from src.cli import CLI

def main():
    bank = BankSystem()
    cli = CLI(bank)
    cli.run()

if __name__ == "__main__":
    main()