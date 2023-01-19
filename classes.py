class Panda:


    def __init__(self, name : str, age : int, gender : str, weigh : int):
     self.name = name
     self.age = age
     self.gender = gender
     self.weigh  = weigh

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

panda1 = Panda("bobe", 3, "Male", 100)
panda2 = Panda("lazyladY", 12, "Female", 80)
panda3 = Panda("soso", 6 , "Female", 60)
panda4 = Panda("pebo", 7, "Male", 120)


panda1.eat("bamboo")
panda1.sleep()

panda2.eat("fruits")
panda2.sleep()

panda3.eat("leaves")
panda3.sleep()

panda4.eat("vegetables")
panda4.sleep()