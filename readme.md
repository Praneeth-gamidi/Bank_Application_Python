Banking Application

A simple command-line banking application built with Python and Object-Oriented Programming (OOP). The application uses the file system for persistent account storage instead of a database and provides core banking operations through a CLI.

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
Error handling for invalid banking operations
No GUI
No database
Technologies Used
Python
Object-Oriented Programming
Command Line Interface (CLI)
File System Storage
pathlib
datetime
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

The application follows a simple layered architecture:

User
  |
  v
CLI
  |
  v
Authentication / Bank System
  |
  v
Account
  |
  v
File Handler
  |
  v
File System
main.py

The main entry point of the application.

It creates the BankSystem and CLI objects and starts the application.

cli.py

Handles user interaction and the command-line menus.

Responsibilities:

Display menus
Collect user input
Display results and errors
Call authentication and banking services

The CLI does not directly manipulate files or implement banking rules.

account.py

Contains the Account class and account-level operations.

Responsibilities:

Store account information
Maintain account balance
Validate withdrawals
Process deposits and withdrawals
Verify PIN
auth_service.py

Handles authentication-related operations.

Responsibilities:

Register new accounts
Generate unique account numbers
Login users
Verify account credentials
bank_system.py

Acts as the main banking service layer.

Responsibilities:

Load accounts
Save accounts
Check account existence
Process deposits
Process withdrawals
Process transfers
Retrieve transaction history
file_handler.py

Handles all raw file-system operations.

Responsibilities:

Check whether an account file exists
Read account files
Write account files
Append transaction records
File Storage

The application does not use a database.

Each account is stored in an individual text file using the account number as the filename.

For example:

src/data/accounts/1571492716.txt

Each account file contains both profile information and transaction history.

Example:

AccountNumber: 1571492716
Name: Karthik
PIN: 8497
Balance: 2000.0
TRANSACTIONS:
2026-08-11 23:47:28,DEPOSIT,2000.0,4000.0
2026-08-11 23:47:36,WITHDRAW,1000.0,3000.0
2026-08-11 23:48:11,TRANSFER_OUT,1000.0,2000.0
2026-08-11 23:48:11,TRANSFER_IN,1000.0,2000.0
Transaction Format

Each transaction follows this format:

timestamp,transaction_type,amount,balance_after

Examples:

2026-08-11 23:47:28,DEPOSIT,2000.0,4000.0
2026-08-11 23:47:36,WITHDRAW,1000.0,3000.0
2026-08-11 23:48:11,TRANSFER_OUT,1000.0,2000.0
2026-08-11 23:48:11,TRANSFER_IN,1000.0,2000.0
Running the Application

Make sure Python is installed on your system.

From the project root directory, run:

python main.py

The application starts with the following menu:

===== BANKING APPLICATION =====

1. Register
2. Login
3. Exit

After successful login, the account menu is displayed:

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

Deposit successful.
New balance: 2500.0
Withdraw
Enter withdrawal amount: 200

Withdrawal successful.
New balance: 2300.0
Transfer
Enter receiver account number: 1234567890
Enter transfer amount: 500

Transfer successful.
New balance: 1800.0
Transaction History
===== TRANSACTION HISTORY =====

2026-08-11 23:47:28,DEPOSIT,500.0,2500.0
2026-08-11 23:50:10,WITHDRAW,200.0,2300.0
2026-08-11 23:52:30,TRANSFER_OUT,500.0,1800.0
Design Principles

The application was intentionally designed to remain simple and easy to understand.

Command-line interface instead of GUI
File-system storage instead of a database
Object-oriented design
Separation of responsibilities
Banking logic separated from user interaction
File operations isolated in file_handler.py
Account-specific operations handled by Account
Banking workflows handled by BankSystem
Authentication handled by auth_service.py
Error Handling

The application handles common invalid operations, including:

Non-existent account
Incorrect PIN
Invalid deposit amount
Invalid withdrawal amount
Insufficient account balance
Non-existent receiver account
Transfer to the same account
Invalid transfer amount

Failed banking operations do not create transaction records.

Persistence

Account information is stored directly on the file system.

For example:

Register account
       |
       v
1571492716.txt
       |
       v
Deposit / Withdraw / Transfer
       |
       v
Updated account file

The data remains available after the application is closed and restarted.

Limitations

This application is designed for educational purposes and is not suitable for real banking or financial use.

The current implementation uses plain-text files, which means:

PINs are not securely hashed or encrypted
Account files do not have database-level access control
File storage does not provide database transactions
Concurrent access is not handled
A system failure during a transfer could potentially result in a partial update
There is no production-grade authentication or authorization system

These limitations are intentional because the project requirements specify a simple CLI-based application using the file system instead of a database.

Future Improvements

Possible improvements include:

Secure PIN hashing
Stronger input validation
Atomic file operations
Transaction rollback for failed transfers
Unit and integration tests
Application logging
Improved transaction formatting
Administrative functionality
Database integration
Better authentication and authorization
Encryption of sensitive account information
Disclaimer

This project is created for learning and demonstration purposes.

It is not intended to process real money, store real financial information, or be used as a production banking system.
