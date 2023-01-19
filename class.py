'''
Using what you learned about classes , create a class to represent a Panda. The class should have the following:

    4 Attributes
    2 Methods

Create 4 instances of the class Panda , print 1 attribute value, and call the two methods on each instance.
'''

class Panda:

    origin = "animal"

    def __init__(self, name , age: int , type: str  , country: str):
        self.name = name
        self.age = age
        self.type = type
        self.country = country 
        
    def type_panda(self):
        return f"{self.country} is the main country for {self.name}"

    def func(self):
        return f"{self.name} old {self.age} type : {self.type}"
    

pand1 = Panda("panda 1", 5 , "Giant panda " ,"China")
pand2 = Panda("panda 2" , 3,"red panda" , "India")
pand3 = Panda("panda 3" ,7 ,"Giant panda" , "malaysa")
pand4 = Panda("panda 4" , 4, "red panda" , "Indonesia")


print(pand1.type_panda())
print(pand1.func())
print("-------------")
print(pand2.type_panda())
print(pand2.func())
print("-------------")
print(pand3.type_panda())
print(pand3.func())
print("-------------")
print(pand4.type_panda())
print(pand4.func())



