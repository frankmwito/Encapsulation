# Bank Account Encapsulation

class BankAccount:
    def __init__(self, name, account_number, account_type, bank_name):
        self.__name = name
        self.__account_number = account_number
        self.__account_type = account_type
        self.__bank_name = bank_name
        self.__balance = 0.00  # Encapsulated balance
    
    def deposit(self, amount):
        """Adds money to the account."""
        self.__balance += amount
        return f"Deposited {amount}. New balance is {self.__balance}"
    
    def withdraw(self, amount):
        """Subtracts money from the account, if enough balance is available."""
        if amount > self.__balance:
            return "Insufficient balance"
        self.__balance -= amount
        return f"Withdrew {amount}. New balance is {self.__balance}"
    
    def get_balance(self):
        """Returns the current balance. Account number is validated."""
        return f"Account Balance: {self.__balance}"
    
# Example usage
account1 = BankAccount("John Doe", "123456789", "Savings", "Bank XYZ")

# Deposit money
print(account1.deposit(500))

# Withdraw money
print(account1.withdraw(200))

# Get balance
print(account1.get_balance())


