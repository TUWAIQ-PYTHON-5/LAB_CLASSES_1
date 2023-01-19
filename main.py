class Panda:

    king:str="animal"
    feet:int=4
    ears:int=2

    def __init__(self, type:str, age:int,weight:float):
            self.type = type
            self.age = age
            self.weight = weight

    def print_panda_info(self):
        return f"Type : {self.type} Age : {self.age} Weight : {self.weight}"

    def print_all_info(self):
        return f"King : {self.king} Feet : {self.feet}  Ears : {self.ears}\nType : {self.type} Age : {self.age} Weight : {self.weight}"


panda1 = Panda("red",5,57.5)
print(panda1.print_panda_info())
print("================================")
print(panda1.print_all_info())

