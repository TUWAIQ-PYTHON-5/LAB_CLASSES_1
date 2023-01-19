class Panda: 
    kind = "animal" 
    def __init__(self, size : int, gender : str, tall: int, age : int):
        self.size = size
        self.gender = gender
        self.tall = tall
        self.age = age

    def panda_info(self):
        return f"This Panda size {self.size}kg, and gender{self.gender}, and {self.tall}Centimetre,and it's old{self.age} yers "

    
    def is_hungry(self, x:bool ):
        if x == True:
            return  "panda is hungry"
        else :
            return "panda is not hungry"

    def is_sick(self, y:bool):
        if y == True:
            return"panda is sick"
        else: 
            return"panda is Good"   


panda1 = Panda(166 ," male ", 150 , 10)
panda2 = Panda(157 ," male ", 137 , 8)  
panda3 = Panda(151 ," fmale ", 125 , 6)
panda4 = Panda(146 ," fmale ", 99 , 5)

print(" panda1: " , panda1.panda_info())
print(" panda2: " , panda2.panda_info())
print(" panda3: " , panda3.panda_info())
print(" panda4: " , panda4.panda_info())


print(panda1.is_hungry(True))
print(panda1.is_sick(True))
print("-----------------")
print(panda2.is_hungry(False))
print(panda2.is_sick(True))
print("-----------------")
print(panda3.is_hungry(False))
print(panda3.is_sick(False))
print("-----------------")
print(panda4.is_hungry(True))
print(panda4.is_sick(False))
