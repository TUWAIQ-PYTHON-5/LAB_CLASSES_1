

class Panda:
    
    kind = "Animals"

    def __init__(self, place : str, age : int, gender : str,food :str):
        
        self.place = place
        self.age = age
        self.gender = gender
        self.food= food
    
    def hestory_about_panda (self):
        return f"The panda live in {self.place} and the favorate food of it :  {self.food} ."





Panda1 = Panda("Australia",2, "male ", "pamboo")



print(Panda1 . hestory_about_panda())
