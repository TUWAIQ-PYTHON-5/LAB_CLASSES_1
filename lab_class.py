class Animal:
    animal_name="Banda"
    def __init__(self,  size: int, age : int, gender : str,sleep_time :int):
        self.size = size
        self.age = age
        self.gender = gender
        self.sleep_time=sleep_time

    def describe(self):
     return f" Banda size {self.size} , {self.age} years old "
banda1=Animal(70, 9, "Female",2)
banda2 =Animal(120, 18, "Male",3)
print("first Banda size is: " , banda1.size)
print(banda1.describe())
print(banda2.describe())
    