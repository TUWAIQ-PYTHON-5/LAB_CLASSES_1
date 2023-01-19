class Panda:
    kind="animal"
    def __init__(self,name :str,size:str,age:int,gender: str):
        self.name= name
        self.size=size
        self.age=age
        self.gender=gender
    def pandas(self):
        return f"The Name is:{self.name} ,and pand's age is {self.age} and the size of the panda is {self.size} "
    def behavior(self):
        return f"Pandas spend most of the day eating and sleeping"

panda1=Panda("panda1","small",10,"male")
panda2=Panda("panda2","small",5,"female")
panda3=Panda("panda3","small",7,"female")
panda4=Panda("panda4","small",5,"female")


print(panda3.kind)
print(panda3.behavior())
print(panda3.pandas())

print(panda2.behavior())
print(panda2.pandas())

print(panda1.behavior())
print(panda1.pandas())
