'''CC
Q1. Create a Student class and initialize it with a name and roll number.
create an object of that class in the same file and print name and roll
number
(Easy) (5 marks)
Q2. Write the above code to enter details of 10 students, and take input
from the user.
Hint: use loops.
(Easy) (5 marks)
Q3. Make a folder and make it a module in python'''

class Pupil :
    def __init__(self,name,rolln):
        self.name = name 
        self.rollnumber = rolln #rolln is variable which can change as per inputs by user


    def userinput(self): 
        d = {}
        for i in range(1,11):  
            n = input("Your Name=   " )
            r = int(input("Your Roll Number=  "))
            
            d[n] = r
        
        print(d)




             
    
        
         





a = Pupil("Me",3)
print(a.name)
print(a.rollnumber) # object will replace "a" so thats why we can print those name n roll number not dierctly by variables 

c = Pupil("n",7)
c.userinput()


