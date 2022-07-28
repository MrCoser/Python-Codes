
# Online Python - IDE, Editor, Compiler, Interpreter

class Expense_Tracker :
    
    # class attribute
    expense_tracker_version = 0.1
    
    def __init__(self, tracker_category, opening_balance, budget):
        # Instance/Object attributes
        self.tracker_category = tracker_category
        self.opening_balance = opening_balance
        self.budget = budget
        
    # instance method 1
    def get_opening_balance(self):
        return self.opening_balance
    
    # instance method 2
    def check_balance(self, limit = 100000):
        if self.budget >= limit:
            return "All right !!! You're good to go"
        else:
            return "Please check your balance"
        
    @staticmethod
    def convert_amount(amount):
        return float(amount)
        
obj = Expense_Tracker("Personal",100,50000)
obj2 = Expense_Tracker("Professional",1000,320000)

print(obj.get_opening_balance())
print(obj2. get_opening_balance())
print(obj.check_balance())
print(obj2.check_balance())
print(obj.convert_amount(2000))