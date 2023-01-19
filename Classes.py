

class PandaClass:
    kind : str = "Animal"
    species : str = "Mammals"

    def __init__(self, name:str,  zoo:str, favFood:str, favTempurture):
        self.name = name
        self.zoo = zoo
        self.favFood= favFood
        self.favTemp= favTempurture

    def favorites(self):
        return f"This is panda called {self.name},and he like to eat {self.favFood} when the wether at {self.favTemp} degrees."
    
    def location(self):
        return f"{self.name},from {self.zoo} Zoo."



panda1=PandaClass("Hue", "National Park", "Bambo", 22)
panda2=PandaClass("Nun", "East Park", "Wicker", 19)
panda3=PandaClass("Tota", "Grand Park", "Blossoms", 20)
panda4=PandaClass("Juna", "Central Park", "Cane", 21)

print()

print(panda1.favorites())
print(panda1.location())
print("_"*50)

print(panda2.favorites())
print(panda2.location())
print("_"*50)

print(panda3.favorites())
print(panda3.location())
print("_"*50)

print(panda4.favorites())
print(panda4.location())
print("_"*50)