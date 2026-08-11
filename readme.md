# Banking Application

A simple command-line banking application built with Python and Object-Oriented Programming (OOP). The application uses the file system for persistent account storage instead of a database and provides core banking operations through a Command Line Interface (CLI).

---

## Features

* Account Registration: Generates a unique, random 10-digit account number.
* Secure Access: PIN-based login system for registered users.
* Core Banking Operations: Check balance, deposit money, and withdraw money.
* Fund Transfers: Direct transfers between different accounts.
* Transaction Tracking: View complete transaction histories.
* Data Persistence: Uses individual text files per account instead of a traditional database.
* Isolated Records: Separate transaction history logs inside each account file.
* Robust Error Handling: Safeguards against invalid banking operations.
* Lightweight Build: Pure CLI execution with no heavy GUI or external database dependencies.

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Command Line Interface (CLI)
* File System Storage (pathlib, datetime)

---

## Project Structure

```text
Banking_App_Python/
│
├── main.py
├── README.md
│
└── src/
    ├── __init__.py
    ├── account.py
    ├── auth_service.py
    ├── bank_system.py
    ├── cli.py
    ├── file_handler.py
    │
    └── data/
        └── accounts/
            └── <account_number>.txt
```

---

## Architecture and Component Responsibilities

The application follows a simple layered architecture where the user interacts with the CLI, which talks to the Authentication and Bank System layers. The Bank System manipulates the Account class, and data is managed by the File Handler on the File System.

### Component Breakdown

* **main.py**: The central entry point. Instantiates the BankSystem and CLI objects to launch the app.
* **cli.py**: Handles user interaction. Displays menus, collects input, shows results or errors, and triggers downstream services.
* **account.py**: Contains the Account class. Manages account states, balance updates, and PIN verifications.
* **auth_service.py**: Manages authentication workflows, handles user log-ins, and provisions new accounts.
* **bank_system.py**: The core logic layer. Manages transfers, batch updates, and coordinates account loading and saving.
* **file_handler.py**: Direct file-system interface. Reads, writes, checks existence, and appends raw data to files.

---

## File Storage and Data Format

The application bypasses traditional databases, using flat text files stored by account number instead.

File Path Example: `src/data/accounts/1571492716.txt`

### Account File Structure Example

```text
AccountNumber: 1571492716
Name: Karthik
PIN: 8497
Balance: 2000.0
TRANSACTIONS:
2026-08-11 23:47:28,DEPOSIT,2000.0,4000.0
2026-08-11 23:47:36,WITHDRAW,1000.0,3000.0
2026-08-11 23:48:11,TRANSFER_OUT,1000.0,2000.0
2026-08-11 23:48:11,TRANSFER_IN,1000.0,2000.0
```

### Transaction String Schema

```text
timestamp,transaction_type,amount,balance_after
```

---

## Running the Application

Ensure Python 3 is installed on your local environment. Run the entry point from your project root directory:

```bash
python main.py
```

### User Interface Menus

Main Menu:

```text
===== BANKING APPLICATION =====
1. Register
2. Login
3. Exit
```

Account Operations Menu:

```text
===== ACCOUNT MENU =====
1. Check Balance
2. Deposit
3. Withdraw
4. Transfer
5. Transaction History
6. Logout
```

---

## Example Workflow

```text
# 1. Registration
Enter your choice: 1
Enter your name: Karthik
Enter your PIN: 8497
Enter initial balance: 2000

Account created successfully.
Your account number is: 1571492716

# 2. Login
Enter your choice: 2
Enter account number: 1571492716
Enter PIN: 8497

Welcome, Karthik!

# 3. Deposit
Enter deposit amount: 500

Deposit successful.
New balance: 2500.0

# 4. Withdrawal
Enter withdrawal amount: 200

Withdrawal successful.
New balance: 2300.0

# 5. Fund Transfer
Enter receiver account number: 1234567890
Enter transfer amount: 500

Transfer successful.
New balance: 1800.0

# 6. Check Transaction History
===== TRANSACTION HISTORY =====
2026-08-11 23:47:28,DEPOSIT,500.0,2500.0
2026-08-11 23:50:10,WITHDRAW,200.0,2300.0
2026-08-11 23:52:30,TRANSFER_OUT,500.0,1800.0
```

---

## Design Principles and Error Handling

### Design Core

* Keep it Simple: Clean CLI layout and flat-file infrastructure for minimal overhead.
* Separation of Concerns: Business logic, file execution, and CLI render components do not mix.

### Error Guardrails

The application proactively traps invalid user choices or illegal workflows. Failed actions do not write records to the log files. Handled faults include:

* Non-existent account inputs
* Incorrect PIN entries
* Negative or zero-value deposit or withdrawal inputs
* Insufficient account balances
* Transfer requests pointing to self or non-existent recipients

---

## Limitations and Future Improvements

### Current Limitations

This project is built strictly for educational demonstration.

* Security: PINs are saved in raw text and lack secure hashing or encryption patterns.
* Concurrency: Missing database-level file locks or transaction rollback mechanics. System disruption mid-transfer could cause partial text data drops.

### Future Roadmap

* Implement secure SHA-256 PIN hashing.
* Integrate atomic file management tools to prevent partial transfers.
* Introduce comprehensive unit and integration testing frameworks.
* Migrate storage to a proper relational engine like SQLite.

---

## Disclaimer

This project is created strictly for learning and demonstration purposes. It is not built to store real financial information, process actual money, or act as a production-grade secure application.
