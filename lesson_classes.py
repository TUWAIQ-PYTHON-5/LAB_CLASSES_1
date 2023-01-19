


class Panda:
    kind = "anamel"

    def __init__(self, contry :str , type :str, size :int, age: int):
        self.contry = contry 
        self.type = type
        self.size = size
        self.age = age
    def panda_self (self):
        return f"We have a panda from the contry of {self.contry} and it is considered to be of the {self.type} and is considered one of the huge animals, as its size is {self.size} and its age is {self.age} years old"

panda1 = Panda("Southern China" , "chinese Panda" , 3 , 18)
panda2 = Panda("Southern Amirca" , " Red Panda" , 2 , 18)
panda3 = Panda("Himalayas ", "White Panda" , 3 , 2)
panda4 = Panda("Nepal" , "Big Panda" , 8 , 20)

print("the first Panda From: " , panda1.contry)
print("the Southern Amirca is a type of", panda2.type)
print("the big Panda considered one of the huge animals, as its size is " , panda4.size, "feet")
print("the baby Panda at age", panda3.age,"years the size is ", panda3.size,"feet")
