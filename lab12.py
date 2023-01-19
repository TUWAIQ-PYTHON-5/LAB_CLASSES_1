class Panda:
    color="white"
    def __init__(self, gender:str, age :int ,height:int, weight:int):
        self.gender=gender
        self.age=age
        self.height=height
        self.weight=weight

    def introduce_self(self):
        return f"the gender panda is {self.gender} and ther age is {self.age} years old"



panda1=Panda("female",7,110,100)
panda2=Panda("male",10,170,180)
panda3=Panda("female",5,112,70)
panda4=Panda("female",20,170,150)
print("panda gender is",panda1.gender,"and height is",panda1.height)
print("panda age is",panda2.age,"and weight is", panda2.weight)
print("the color of all panda is",Panda.color)
print(panda4.introduce_self())
