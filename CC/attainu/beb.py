# difference btw inheritance n import
from inheritfile import Parents

class Beb(Parents):
    def __init__(self,height,hairtype,features,name):
        self.name = name   
        super().__init__(height, hairtype, features,)


       # to inherit attributes we need super class function super(). 

    def mine(self,name):
        print(f"{name} is mine") #to make variable private __ using two underscore before it acess modifier

    def habbits(self):
        print("i m his habbit")  
        super().habbits() #super(). is also used for access same function from parents class too it will write both overriding     


aaina = Beb(6,"black","sharp","kub")
print(aaina.name)
aaina.habbits()
aaina.mine("kub")
a = Parents(5.11,"black silky","sharp") # as we imported this class we cant apply parent method(f) on same  host class object of child
'''a.habbits()''' #but we can access functions(methods of parents class) directly 


