
# Online Python - IDE, Editor, Compiler, Interpreter

class Expense_Tracker :
    
    # class attribute
    expense_tracker_version = 0.1
    
    def __init__(self, tracker_category, opening_balance, budget):
        # Instance/Object attributes
        self.tracker_category = tracker_category
        self.opening_balance = opening_balance
        self.budget = budget
        
home_tracker = Expense_Tracker("Home", 0, 3000)
shopping_tracker = Expense_Tracker("Shopping", 1000, 30000)

## Example to establish the difference between class and
## instance attributes
print(home_tracker.opening_balance)
print(shopping_tracker.opening_balance)
print(home_tracker.expense_tracker_version)
print(shopping_tracker.expense_tracker_version)

## Since both of the values of expense_tracker_version did not change,
## this proves that the class attributes never change with class objects, whereas
## the instance attributes will change with every object instance created