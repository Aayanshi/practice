#doubt i wala secene kyun nahi aa skta
count = 0
while(True):
    n1 = int(input("guess no.= "))
    count = count + 1
    if n1 == 17:
        print("you got it right", count , "guesses you took ")
        break  
    elif n1 > 17:
        print("too high! like your dreams" ,3-count,"guesses are left" )  
        continue 
    elif count == 3:
        print("game overrrr")   
    else:
        n1 < 17
        print("too low like your standards", 3-count,"guesses are left")
        continue
            


    
  