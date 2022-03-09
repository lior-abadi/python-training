class Account:
    
    # This is the constructor of the class (similar to the constructor of smart contracts)
    def __init__(self, filepath):
        self.filepath = filepath
        with open(self.filepath, "r") as file:
            self.balance = float(file.read())
    
    def withdraw(self, amount):
        self.balance -= amount
        self.commit()
        print("Withdrawal Successful. New balance: ", self.balance)
    
    def deposit(self, amount):
        self.balance += amount    
        self.commit()
        print("Deposit Successful. New balance: ", self.balance)
        
    def commit(self):
        with open(self.filepath, "w") as file:
            file.write(str(self.balance))
    

# By passing to the child the parent class an inheritance is created. 
class Checking(Account):
    # This constructor structure establishes an inheritance of the Account class. Checking is a child of Account.
    def __init__(self, filepath, fee):
        self.fee = fee
        Account.__init__(self, filepath)
    
    def transfer(self, amount, to):
        if self.balance < amount:
            print("Insufficient funds to make this transfer.")
        else:     
            self.balance -= (amount-self.fee)
            print("Transfer successful. Sent: ", amount, " to: ", to, ". Current Balance: ", self.balance)
            print("Fees charged: ", self.fee)
            checking.commit()
    
    
    
checking = Checking("balance.txt")  
checking.deposit(100)
checking.transfer(1280, "Robertito")