class Pandas :
    kind = "Animal"
    def __init__(self, name : str, gender : str ,  hobby : int , age :int ):
        #initialize object / instance attributes
        self.name = name
        self.gender = gender
        self.hobby = hobby
        self.age = age
    print("Hello this is a Panda Sanctuaries!! , \n we have many pandas, let me introduse you to some of them : ")
    def my_panda(self):
        return f" we have {self.name} and it is  {self.age} years old ,it is a {self.gender}, and finally it like to {self.hobby} "
#to create a new object/instance from the class Person
panda1 = Pandas("LORI", "female", "sleep" , 3 )
panda2 = Pandas("LazyLady", "female", "eat" , 4 )
panda3 = Pandas("MEME", "female", "play" , 2 )
#to read an isntance attribute
p1= (panda1.my_panda())
p2= (panda2.my_panda())
p3= (panda3.my_panda())
#calling a method
print(p1)
print(p2)
print(p3)
