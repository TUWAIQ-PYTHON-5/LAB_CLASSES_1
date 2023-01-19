class Panda :
    kind = "animal"

    def __init__(self, color : str, height : int , gender : str, age : str):
        
        self.color = color
        self.height = height
        self.gender = gender
        self.age = age

    def introduce_the_panda(self):
        return f"The panda color : {self.color} , his {self.height} , gender : {self.gender} and the age : {self.age}"

Describe1 = Panda("White" , 160 , "Man" , "1 year")
Describe2 = Panda("White and balck" , 50 , "Man" , "1 mounth") 


print(Describe1.introduce_the_panda())

print(Describe2.introduce_the_panda())
