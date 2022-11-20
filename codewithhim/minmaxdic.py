class MinMax:
    def __init__(self):
        pass 


    def Maxima(self):
        print("lets find Maximum Qualities of yours")
        d = { }
        for i in range(1,5):
            n = (input("Your Best Qualities Please=  "))
            p = int(input("How much do you have=  "))
            d[n] = p
        mx = float('-inf')   #very big 
        it = ""
        for i in d.keys():
            if mx < d[i] :
                mx = d[i]
                it = i
            else:
                continue   
        print(it,"its your best one be proud of" ,mx) 
        print(d)     

    def Minima(self):
        print("lets see What you have bare Minimum")
        d = { }
        for i in range(1,5):
            n = (input("Your Worst traits=  "))
            p = (int(input("how much do you have= ")))
            d[n] = p
        mi = float('-inf')   # very small
        it = ""
        for i in d.keys():
            if mi < d[i]:
                mi = d[i]
                it = i
            else :
                continue
        print(f"{i} we need work on it {min}")  
        print(d)      




       
a = MinMax()  
a.Maxima() 
a.Minima()



