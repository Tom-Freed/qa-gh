# Goal: “Create a Budget class that can instantiate 
# objects based on different budget categories 
# like food, clothing, and entertainment. 
# These objects should allow for depositing and 
# withdrawing funds from each category, 
# as well computing category balances and transferring 
# balance amounts between categories”

class Budget:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"£{amount:.2f} was deposited in {self.name}\n{self.name} balance: £{self.balance:.2f}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficent funds in {self.name}")
        else:
            self.balance -= amount
            print(f"£{amount:.2f} was withdrawn from {self.name}\n{self.name} balance: £{self.balance:.2f}")

    def show_balance(self):
        print(f"{self.name} balance: £{self.balance:.2f}")

    def transfer_balance(self, category, amount):
        if amount > self.balance:
            print(f"Insufficent funds in {self.name}")
        else:
            self.withdraw(amount)
            category.deposit(amount)
            print(f"""£{amount:.2f} was transfered to {category.name}
Current balance in {self.name} is £{self.balance:.2f}
Current balance in {category.name} is £{category.balance:.2f}""")

food = Budget('food')
clothing = Budget('clothing', 100)
entertainment = Budget('entertainment')

food.deposit(50)

clothing.withdraw(200)

clothing.transfer_balance(entertainment, 50)

entertainment.show_balance()
        
