'''Create a class Speed and add a method to convert speed from
kilometers per hour to meter per sec'''

#ans3.
class Speed:
    def __init__(self):
        '''self.distance =distance
        self.time= time
        self.speed = speed'''


    def Speedcal(self):
        d = int(input("enter your Distance u have travelled= "))
        t = int(input("enter your Time you have taken =  "))
        s = d / t 
        print(f"{s} the speed u have achived")

    def convertspeed (self):
        e = int(input("Your Speed in km/hr= "))
        m = e * 5/18 
        print(f"Your Speed in m/s is = {m}")



        
        
        

a = Speed()
a.Speedcal()
print()
a.convertspeed()

