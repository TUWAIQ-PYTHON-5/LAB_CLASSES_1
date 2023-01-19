class Panda:

    kind = "animal"
    color = "White and Black"
    def __init__(self, name : str, age : int, gender : str, wight : str, fevActivity : str):
        self.name = name
        self.age = age
        self.gender = gender
        self.wight = wight
        self.fevActivity = fevActivity

    def identification(self):
        return f"Name: {self.name} \nAge: {self.age} \nGender: {self.gender} \nWight: {self.wight}"

    def activities(self):
        return f"{self.name} like to {self.fevActivity} all the time"


Panda1 = Panda("Po",13,"male","50kg","Play")
Panda2 = Panda("Lily",12,"female","48kg","Play")
Panda3 = Panda("Bob",30,"male","250kg","Sleep")
Panda4 = Panda("Rose",27,"female","200kg","Eat")

print(f"All the Panda are {Panda.color}")

print(Panda1.identification())
print(Panda1.activities())
print("--"*10)
print(Panda2.identification())
print(Panda2.activities())
print("--"*10)
print(Panda3.identification())
print(Panda3.activities())
print("--"*10)
print(Panda4.identification())
print(Panda4.activities())
