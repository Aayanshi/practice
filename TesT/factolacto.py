''' Write A Python Program For Class "FactoLacto" Which Have A Method Which Print The Factorial Of The User Integer Input.
inherit it in a child class
 input= 5
 5*4*3*2*1
 output = 120
'''


class FactoLacto:
    
        
    def Fucktorial(self):
        c = 1
        n = int(input("Enter your number= "))
        for i in range(1,n+1):
            c = c*i 
            

        
        
        print(c)    


obj = FactoLacto()
obj.Fucktorial()


