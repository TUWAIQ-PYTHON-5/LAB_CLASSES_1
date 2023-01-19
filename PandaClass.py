

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

panda1 = Panda("A", 15, "Male", 80)
panda2 = Panda("B", 22, "Female", 90)
panda3 = Panda("C", 9 , "Female", 60)
panda4 = Panda("D", 7, "Male", 88)


panda1.eat("bamboo")
panda1.sleep()

panda2.eat("fruits")
panda2.sleep()

panda3.eat("leaves")
panda3.sleep()

panda4.eat("vegetables")
panda4.sleep()