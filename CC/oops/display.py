class Display :
    def __init__ (self,name,last_name,occupation,byear):
        self.name = name           #use same kind of varriable with same name of attribute
        self.lastname = last_name
        self.occupation = occupation
        self.byear = byear

    def setage(self,a): #introduced new attribute inside a method
        self.age = a
        print(f"this is your age= {a}")   

    def profile(self):
        print(f" Name = {self.name} \n Last Name = {self.lastname} \n Occupation = {self.occupation} \n Birthyear = {self.byear}  \n ")     
    
    def marks(self,m): 
        self.m = m
        print(f"Total Marks = {m}")

ob = Display("Ram","Sharma","Devloper","2000")

ob.profile()  
ob.marks(300) #put value inside the varible 
ob.setage(20)
