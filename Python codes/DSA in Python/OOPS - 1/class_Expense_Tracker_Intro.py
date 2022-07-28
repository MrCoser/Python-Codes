
# Online Python - IDE, Editor, Compiler, Interpreter

class ExpenseTracker :
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount
    
obj1 = ExpenseTracker("12 Feb","Going on a Party", "10000")
print(obj1.date)
print(obj1.amount)