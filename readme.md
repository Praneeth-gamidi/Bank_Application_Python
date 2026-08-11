Banking Application

A simple command-line banking application built with Python and Object-Oriented Programming. The application uses the file system for persistent account storage instead of a database and provides core banking operations through a CLI.

Features

Account registration with a randomly generated 10-digit account number

PIN-based login

Check account balance

Deposit money

Withdraw money

Transfer money between accounts

View transaction history

Persistent account data using individual text files

Separate transaction history for each account

Input and error handling through the CLI

Technologies Used

Python

Object-Oriented Programming (OOP)

File System Storage

Command Line Interface (CLI)

Python pathlib

Python datetime

Project Structure

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

Architecture

The application follows a simple layered design:

User
  ↓
CLI
  ↓
Authentication / Bank System
  ↓
Account
  ↓
File Handler
  ↓
File System

main.py

Acts as the application entry point. It creates the BankSystem and CLI objects and starts the application.

cli.py

Handles user interaction, menus, input collection, and displaying results. It does not directly manipulate account files or implement banking rules.

account.py

Contains the Account class and account-level operations such as:

Deposit validation

Withdrawal validation

PIN verification

Balance management

auth_service.py

Handles authentication-related operations:

Account registration

Account login

Account number generation

PIN verification through the Account class

bank_system.py

Acts as the main banking service layer. It handles:

Loading and saving accounts

Deposits

Withdrawals

Transfers

Transaction history

Account existence checks

file_handler.py

Handles raw file-system operations. It is responsible for:

Checking account files

Reading account files

Writing account files

Appending transaction records

File Storage

No database is used.

Each account is stored in a separate text file using its account number as the filename.

For example:

data/accounts/1571492716.txt

A typical account file looks like:

AccountNumber: 1571492716
Name: Karthik
PIN: 8497
Balance: 2000.0
TRANSACTIONS:
2026-08-11 23:47:28,DEPOSIT,2000.0,4000.0
2026-08-11 23:47:36,WITHDRAW,1000.0,3000.0
2026-08-11 23:48:11,TRANSFER_OUT,1000.0,2000.0

The account profile and transaction history are stored together in the same file.

Transaction Format

Transactions follow this format:

timestamp,transaction_type,amount,balance_after

Examples:

2026-08-11 23:47:28,DEPOSIT,2000.0,4000.0
2026-08-11 23:47:36,WITHDRAW,1000.0,3000.0
2026-08-11 23:48:11,TRANSFER_OUT,1000.0,2000.0
2026-08-11 23:48:11,TRANSFER_IN,1000.0,2000.0

Running the Application

Make sure Python is installed.

From the project root:

python main.py

The application starts with:

===== BANKING APPLICATION =====

1. Register
2. Login
3. Exit

After login, the account menu provides:

===== ACCOUNT MENU =====

1. Check Balance
2. Deposit
3. Withdraw
4. Transfer
5. Transaction History
6. Logout

Example Workflow

Register

Enter your choice: 1
Enter your name: Karthik
Enter your PIN: 8497
Enter initial balance: 2000
Account created successfully.
Your account number is: 1571492716

Login

Enter your choice: 2
Enter account number: 1571492716
Enter PIN: 8497
Welcome, Karthik!

Deposit

Enter deposit amount: 500
Deposit successful. New balance: 2500.0

Withdraw

Enter withdrawal amount: 200
Withdrawal successful. New balance: 2300.0

Transfer

Enter receiver account number: 1234567890
Enter transfer amount: 500
Transfer successful. New balance: 1800.0

Transaction History

===== TRANSACTION HISTORY =====
2026-08-11 23:47:28,DEPOSIT,500.0,2500.0
2026-08-11 23:50:10,WITHDRAW,200.0,2300.0
2026-08-11 23:52:30,TRANSFER_OUT,500.0,1800.0

Design Principles

The project intentionally keeps the implementation simple.

No GUI

No database

File-system based persistence

OOP-based design

Separation of responsibilities

Banking logic is kept outside the CLI

File operations are isolated in file_handler.py

Account-specific rules are handled by Account

BankSystem coordinates banking operations

Validation and Error Handling

The application handles common invalid operations such as:

Non-existent account

Incorrect PIN

Invalid deposit amount

Invalid withdrawal amount

Insufficient balance

Non-existent receiver account

Transfer to the same account

Failed banking operations should not create transaction records.

Limitations

This application is designed as an educational project and is not suitable for real banking or financial use.

The project intentionally uses plain-text files, which means:

PINs are not securely encrypted or hashed

Account files are not protected with database-level access controls

File storage does not provide database transactions

Simultaneous access is not handled

A system failure during a multi-file transfer could theoretically cause partial updates

These limitations are intentional because the project requirements specify a simple CLI and file-system-based implementation.

Future Improvements

Possible future improvements include:

Secure PIN hashing

Better input validation

Transaction rollback for failed transfers

Atomic file updates

Unit tests

Logging

Improved transaction formatting

More detailed account information

Role-based administration

Migration to a database for production use

Disclaimer

This project is created for learning and demonstration purposes. It is not intended to process real money or store real financial information.