'''Q1. Create a Student class and initialize it with name and roll number.
Make methods to :
1. Display - It should display all the information of the
student. 2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student.'''

class StudentProfile :
    def __init__(self,n,r,b) :
        self.name = n
        self.roll_number = r
        self.birth_year = b
          

    def age(self,b):
        c = 2022 - b   
        print(f"your age is {c}")  

    def marks(self):
        
        m = int(input("your English marks= "))  
        n = int(input("your Maths marks= ")) 
        o = int(input("your Science marks= "))
        p = int(input("your Hindi marks= "))
        d = {}
        d["English"] = m
        d["Maths"] = n
        d["Science"] = o 
        d["Hindi"] = p
                   
        
        print(d)
         
n = input("Your name= ")
r = int(input("your Roll number= "))
b = int(input("Your Birth year= "))

n = StudentProfile(n,r,b)
n.age(b)
n.marks()



        

