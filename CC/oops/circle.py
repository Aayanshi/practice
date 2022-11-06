'''q2 cc of oop w3d5
Create a Circle class and initialize it with radius. Make two methods
getArea and getCircumference inside this class.
'''


class Circles:
    def __init__ (self,p):
        self.radius = p


    def are(self,p):
        a = 3.14 * p * p  
        print(f"here is area of your circle = {a} ")

    def circum(self,p):
        c = 2 * 3.14 * p   
        print(f"here is circumfrence of circle= {c} ") 

p = int(input("put your radius= "))
r = Circles(p) 
r.are(p)      
r.circum(p)
