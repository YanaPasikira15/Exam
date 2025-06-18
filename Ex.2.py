class Logger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.log_file = "bank_transactions.log"
            with open(cls._instance.log_file, "w") as f:
                f.write("Bank Transaction Log\n")
                f.write("====================\n")
        return cls._instance
    def log(self, message):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        print(log_message)  # Print to console
        with open(self.log_file, "a") as f:
            f.write(log_message + "\n")
            
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.logger = Logger()
        self.logger.log(f"Account {self.account_number} created with initial balance: {self.balance}")
    
    def deposit(self, amount):
        if amount <= 0:
            self.logger.log(f"Deposit failed: Invalid amount {amount}")
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.logger.log(f"Account {self.account_number}: Deposited {amount}. New balance: {self.balance}")
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            self.logger.log(f"Withdrawal failed: Invalid amount {amount}")
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            self.logger.log(f"Account {self.account_number}: Withdrawal failed. Insufficient funds for {amount} (balance: {self.balance})")
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.logger.log(f"Account {self.account_number}: Withdrew {amount}. New balance: {self.balance}")
        return self.balance
    
    def get_balance(self):
        return self.balance

if __name__ == "__main__":
    try:
        account1 = BankAccount("ACC123", 1000)
        account2 = BankAccount("ACC456", 500)
        
        account1.deposit(200)
        account2.deposit(300)
        
        account1.withdraw(150)
        account2.withdraw(100)
        
        try:
            account1.withdraw(2000)
        except ValueError as e:
            print(f"Expected error: {e}")
        
        try:
            account2.deposit(-100)
        except ValueError as e:
            print(f"Expected error: {e}")
            
        print(f"Account {account1.account_number} balance: {account1.get_balance()}")
        print(f"Account {account2.account_number} balance: {account2.get_balance()}")
        
    except Exception as e:
        print(f"Unexpected error: {e}")
