class Panda :
    kind = "animal"

    def __init__(self, name : str, age : int, height : int) :
        self.name = name
        self.age = age
        self.height = height
    
    def pandaInformation(self) :
        print (f"kind : {self.kind}, name : {self.name}, age : {self.age} years old")

    def pandaHeight(self) :
                print (f"Height : {self.height} cm")
    
panda1 = Panda("X111", 5, 110)
panda2 = Panda("X222", 8, 130)
panda3 = Panda("X333", 12, 180)
panda4 = Panda("X444", 2, 80)

print()
print(f"Panda Age : {panda2.age}")
print()

panda1.pandaInformation()
panda1.pandaHeight()
print()
panda2.pandaInformation()
panda2.pandaHeight()
print()
panda3.pandaInformation()
panda3.pandaHeight()
print()
panda4.pandaInformation()
panda4.pandaHeight()
print()



