
# Online Python - IDE, Editor, Compiler, Interpreter

## This program is made to show attributes of a class
## and it's associated functions

# declaring a class
class Expense_Tracker :
    
    # class-attribute
    expense_tracker_version = 0.1
    
    def __init__(self, opening_balance, tracker_category, budget):
        self.opening_balance = opening_balance
        self.tracker_category = tracker_category
        self.budget = budget
        
# printing attributes and their respective values
home_tracker = Expense_Tracker("1500", "Credit", "30000")
print(home_tracker.tracker_category)

shopping_tracker = Expense_Tracker("2500", "Debit", "30000")
print(shopping_tracker.tracker_category)

# __dict__ prints a dictionary having the attributes, with 
# the keys being the values of these attributes
print(home_tracker.__dict__)
print(shopping_tracker.__dict__)

# getattr() prints the value of the specified attribute
print(getattr(home_tracker, 'opening_balance'))
print(getattr(shopping_tracker, 'opening_balance'))

# hasattr() prints True or False, corresponding to whether
# the attribute is present in the class or not
print(hasattr(home_tracker, 'opening_balance'))
print(hasattr(shopping_tracker, 'debit'))