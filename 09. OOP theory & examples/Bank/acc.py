

class Account:
    
    def __init__(self, filepath):
        with open(filepath, "r") as file:
            self.balance = float(file.read())
    
    
account = Account("balance.txt")
print(account)        