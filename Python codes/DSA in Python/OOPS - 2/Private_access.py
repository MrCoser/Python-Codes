
# Online Python - IDE, Editor, Compiler, Interpreter

# Parent Class
class Vehicle():
    def __init__(self, make, model, fuel):
        self.make = make
        # private
        self.__model = model
        self.__fuel = fuel
   
    def __private_method_parent(self):
       print("This attribute is private")
# Child Class
class Car(Vehicle):
    def __init__(self, make, model, fuel, air_conditioning, sunroof):
        # Parent Attributes
        Vehicle.make = make
        Vehicle.__model = model
        Vehicle.__fuel = fuel
        
        # Child Attributes
        self.air_conditioning = air_conditioning
        self.sunroof = sunroof
    
    def show_parent_attribute(self):
        print(Vehicle.make, " ", Vehicle.__model, " ", Vehicle.__fuel)
        
    def show_private_method_ofparent(self):
        self._Vehicle__private_method_parent()
obj = Car("Tesla",2019,"Electric",True,True)
print(obj.show_private_method_ofparent())