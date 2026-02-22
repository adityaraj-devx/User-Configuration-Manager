class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })
    
    def withdraw(self, amount, description=""):
        if self.get_balance() >= amount:
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)
    
    def transfer(self, amount, category):
        if self.check_fund(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            self.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_fund(self, amount):
        if amount > self.get_balance:
            return False
        return True