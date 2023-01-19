class Anmails:
    Anmail="pinda"
    def __init__(self,size:int,clor:str,height:int,eat:str,Nice:str):
        self.size=size
        self.clor=clor
        self.height=height
        self.eat=eat
        self.Nice=Nice
    def the_pinda(self):
     return f" the pinda in in the forest {self.eat}" 
    def another_pinda(self):
        return f" Characteristics of the panda {self.Nice}" 

pinda1=Anmails(47,"black",70,"herb","kind")
pinda2=Anmails(55,"black with whgite",70,"herb","kind")
pinda3=Anmails(66,"whgite",70,"herb","kind")
pinda4=Anmails(70,"Dark gray",70,"herb","kind")
print("information the anmil",pinda1.clor)
print(pinda1.the_pinda())
print(pinda3.another_pinda())




