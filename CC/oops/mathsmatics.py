class Mathsmatics :
    def __init__(self,num1,num2):
        self.n1 = num1
        self.n2 = num2

    def addition(self,num1,num2):
        c = num1 + num2 
        print(f"The Addition of your Numbers = {c}")

    def multiplictaion(self,num1,num2):
        d = num1 * num2 
        print(f"The multiplication of your Numbers = {d}") 

    def subraction(self,num1,num2):
        e = num1 - num2
        print(f"THE Subtraction of your Numbers= {e}")


num1 = int(input("Your first Number= "))
num2 = int(input("your Second Number= "))

ob = Mathsmatics(num1, num2)  
ob.addition(num1,num2) 
ob.subraction(num1,num2)
ob.multiplictaion(num1,num2)



    
            