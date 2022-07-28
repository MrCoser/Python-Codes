
# Online Python - IDE, Editor, Compiler, Interpreter

# Parent Class
class Vehicle():
    def __init__(self, make, model, fuel):
        self.make = make
        self.model = model
        self.fuel = fuel

# Child Class
class Car(Vehicle):
    def __init__(self, make, model, fuel, air_conditioning, sunroof):
        # Parent Attributes
        Vehicle.make = make
        Vehicle.model = model
        Vehicle.fuel = fuel
        
        # Child Attributes
        self.air_conditioning = air_conditioning
        self.sunroof = sunroof
    
    def show_parent_attribute(self):
        print(Vehicle.make, " ", Vehicle.model, " ", Vehicle.fuel)
        
obj = Car("Tesla",2019,"Electric",True,True)
print(obj.__dict__)
print(obj.show_parent_attribute())
print(obj.make)