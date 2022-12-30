#print numbers from 1 -10



def anyname(i):
    if i == 1:
        return
    print(i,"u can,keep it up")    
    anyname(i-1)

anyname(5)
print("hey, we did it")


# factorial 
n = int(input("here= ")) #3
def factorial(n):      #3
    if n == 1:        #3x2x1 = 6
        return 1
    else:
        c = n * factorial(n-1)    
        return c

d = factorial(n)     
print(d)
