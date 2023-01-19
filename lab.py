class Panda:
    kind = "animal"
    def __init__(self,name:str,age:int,gender:str,Weight:int):
        self.name=name
        self.age=age
        self.gender=gender
        self.Weight=Weight

    def foul(self,foulPanda):
        self.foulPanda=foulPanda
        return f"foul panda is: {foulPanda}"

    def food(self,foodPanda):
        self.foodPanda=foodPanda
        return f"food panda is: {foodPanda}"

panda1=Panda("jeje",10,"Fmale",120)
panda2=Panda("bebe",40,"Male",155)
panda3=Panda("fefe",30,"male",134)
panda4=Panda("rere",20,"fmale",140)



print(panda1.age)
print(panda2.food("reeds"))