class Number:
    def __init__(self,typenumber):
     self.typenumber = typenumber

    def evenodd(self):
        n = int(input("your number please= "))
        if n % 2 ==0 :
            print(f"{n} is even number :)")
        else :
            print(f"{n} is odd number:(" )  

    def primenum(self): 
        print("A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number. 2, 3, 5, 7 etc. ")   
        n1 = int(input("your number here=  "))
        if n1 > 1:
            for i in range(2,n1):
                if n1 % i == 0:
                 print(f"{n1} is not prime number")

                else:
                 print(f"{n1} yesss it is prime number") 
        else:
            print(f"{n1} is not a prime number= ")       



        



a = Number("wholenumber")
print(a.typenumber)

a.primenum()
a.evenodd()

