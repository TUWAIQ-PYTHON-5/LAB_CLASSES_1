
class Panda :
    kind = "animal"

    def __init__(self , tall : int , Gender : str , whight : int , age : int ) -> None:
        self.tall = tall
        self.Gender = Gender
        self.whight = whight
        self.age = age


    def isPandaSick(self , is_sick : bool):
        
        if is_sick == False:
            return "panda is not okay"
        else:
            return"panda is okay"    

    def isPandaAngry(self , is_angry : bool):
        if is_angry == True:
            return "panda is angry"        
        else:
            return"panda is not angry"     



panda1 = Panda( 50 , "male" , 60 , 2)
panda2 = Panda( 60 , "femail" , 30 , 1)
panda3 = Panda( 50 , "male" , 60 , 4)
panda4 = Panda( 40 , "femail" , 66 , 3)


print("Gender :" , panda1.Gender)
print(panda1.isPandaSick(True))
print(panda1.isPandaAngry(False))
print("____"*10)
print("age : " ,  panda2.age)
print(panda2.isPandaSick(False))
print(panda2.isPandaAngry(False))
print("____"*10)
print("tall is :" , panda3.tall)
print(panda3.isPandaSick(True))
print(panda3.isPandaAngry(True))
print("____"*10)
print("whight is :" , panda4.whight)
print(panda4.isPandaSick(True))
print(panda4.isPandaAngry(False))


