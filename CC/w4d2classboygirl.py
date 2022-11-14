'''Describe in detail all the concepts of OOPS with code examples.
'''
# there are four principles
# 1. Encapsulation (class)
# 2. Inheritance   (merging and modifing classes together its not importing them )
# 3. Abstraction   (hiding some details or calculation from user, other programer)
# 4. Polymorphism   (same thing but different forms)

class BoyGirl :
    def __init__(self,x,y):
        self._x = x
        self.y = y

    def Gender_Founder(self):
        n = input("enter your gene factors -> ")
        if n == "XX" or n == "xx":
            print("You are lucky 'Girl'")
        elif n == "XY" or n == "xy":
            print("You are poor 'Boy'")  
        else:
            print("You are someone who is beyond these bars")    
    
    
    print()


    def Future_baby_Gender(self):
        print("see accept whatever u will get by heart but i still hope you a baby girl")
        n = input("Father genes-> ") # xy   
        p = input("Mother genes-> ") #xx
        for i in n:
            for j in p:
                c = i + j
                if c == "xx":
                    print("it can be a Girl too")
                    break
                else:
                    print("it can be a Boy too") 
                    break
        print("better to use protection, cause even god cant tell this duh!!!!")        
    
    print()


class GeneFactors(BoyGirl): #inheritance

    def Gene_Factors(self):
        for i in range(3):
             print("write for female- 'F' \n for male- 'M'\n")
             n = input("Your Gender please=  \n ")    
             if n == "F":
                print("you have'XX'Genes not like your toxic EX") 
             elif n == "M" :
                 print("you have 'XY' Genes but why?") 
             else:
                print("you are He/She , i m also still figuring out")       

        

a = BoyGirl("xx","xy") #polymorphism
a.Future_baby_Gender()
a.Gender_Founder()
a = GeneFactors("x","y")
a.Gene_Factors()


