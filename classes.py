class Panda:

    kind = "animal"
    color = "White and Black"
    def __init__(self, name : str, age : int, gender : str, wight : str):
        self.name = name
        self.age = age
        self.gender = gender
        self.wight = wight

    def identification(self):
        return f"Name: {self.name} \nAge: {self.age} \nGender: {self.gender} \nWight: {self.wight}"


Panda1 = Panda("Po",13,"male","50kg")
Panda2 = Panda("Lily",12,"female","48kg")
Panda3 = Panda("Bob",30,"male","250kg")
Panda4 = Panda("Rose",27,"female","200kg")

print(f"All the Panda are {Panda.color}")

print(Panda1.identification())
print("--"*10)
print(Panda2.identification())
print("--"*10)
print(Panda3.identification())
print("--"*10)
print(Panda4.identification())
