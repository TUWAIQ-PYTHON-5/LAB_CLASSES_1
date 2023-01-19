class Panda:
    kind = "animals"

    def __int__(self, gender:str, size:int, height:int):
        self.gender = gender
        self.size = size
        self.height = height


    def introduce_self(self):
        return f"hi,I don't move much because of my is {self.size}"
    def gender_self(self):
        return f"hi,I help bring food because im female {self.gender}"

panda1 = Panda("Male", 180, 160)
panda2 = Panda("Female", 125, 150)
panda3 = Panda("Male", 140, 170)
panda4 = Panda("Female", 130, 155)


print("the kind of Panda:",Panda.kind)

