
#to define a class
class Panda:
    #class Attribute / Property
    kind = "Animals"

    def __init__(self, place : str, age : int, gender : str,food :str):
        #initialize object / instance attributes
        self.place = place
        self.age = age
        self.gender = gender
        self.food= food
    
    def hestory_about_panda (self):
        return f"The panda live in {self.place} and the favorate food of it :  {self.food} ."




#to create a new object/instance from the class Person
Panda1 = Panda("Australia",2, "male ", "pamboo")


#calling a method
print(Panda1 . hestory_about_panda())
