class Account:
    def __init__(self, account_number, name, pin, balance):
        self._account_number = account_number
        self._name = name
        self._pin = pin
        self._balance = balance
    #Method to check whether a withdrawal is possible or not 
    def can_withdraw(self, amount):
        return amount > 0 and amount <= self._balance

    #Method to convert account object to string
    def to_line(self):
        return (
            f"AccountNumber: {self._account_number}\n"
            f"Name: {self._name}\n"
            f"PIN: {self._pin}\n"
            f"Balance: {self._balance}"
        )
    def verify_pin(self, pin: str) -> bool:
        return self._pin == pin
    # later: return hash_pin(pin) == self._pin_hash

    #Method to create account object from string
    @classmethod
    def from_line(cls, line):
        lines = line.strip().splitlines()
        account_number = lines[0].split(": ", 1)[1]
        name = lines[1].split(": ", 1)[1]
        pin = lines[2].split(": ", 1)[1]
        balance = float(lines[3].split(": ", 1)[1])
        return cls(account_number, name, pin, balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Please enter a valid amount")
        self._balance += amount

    def withdraw(self, amount):
        if not self.can_withdraw(amount):
            raise ValueError("You don't have enough balance to withdraw")
        self._balance -= amount
