class Student:
    def __init__(self,n,a,y,g) :  #n = input name i will be same on next line 
                                   #self is a repwrsentation of object tell about whichever object call 
        self.name = n #class variable (attributes)
        self.age = a
        self.byear = y #define student
        self.gender = g


    def read(self,g): #class methods (objects actions)
        if g == "female" :
            print(f"student {self.name} is reading soft pink huh novels")   #f =formated string
        else :
            print(f"student {self.name} is reading dark fantansy novels")    

    def write(self):
        print(f"student{self.name} is writing") 

    def test(self):
        print(f"student{self.name} is giving test")       

n = input("your name here= ")
a = int(input("age number= "))
y = int(input("birth year= "))
g = input("gender= ")
n = Student(n,a,y,g)
n.read(g)
n.write()
n.test()

Kabir = Student("kabir", 24,1998)
Aaina = Student("Aaina",20,2002) 
 
Kabir.read()
Aaina.read()
Kabir.test()
Kabir.write()
Aaina.test()



