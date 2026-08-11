from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
ACCOUNTS_DIR = BASE_DIR / "data" / "accounts"

def account_file_exists(account_number: str) -> bool:
    account_file = ACCOUNTS_DIR / f"{account_number}.txt"
    return account_file.is_file()


def read_account_file(account_number: str) -> str:
    account_file = ACCOUNTS_DIR / f"{account_number}.txt"

    if not account_file_exists(account_number):
        raise FileNotFoundError(f"Account file not found: {account_file}")
    with account_file.open("r", encoding="utf-8") as file:
        return file.read()


def write_account_file(account_number: str, content: str) -> None:
    ACCOUNTS_DIR.mkdir(parents=True, exist_ok=True)
    account_file = ACCOUNTS_DIR / f"{account_number}.txt"
    with account_file.open("w", encoding="utf-8") as file:
        file.write(content)


def append_transaction_line(account_number: str, line: str) -> None:
    account_file = ACCOUNTS_DIR / f"{account_number}.txt"
    if not account_file_exists(account_number):
        raise FileNotFoundError(f"Account file not found: {account_file}")
    with account_file.open("a", encoding="utf-8") as file:
        file.write(line + "\n")
