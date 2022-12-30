#### iterate
'''
n = int(input("here number = "))

def factorial(n): #3
    if n == 1 :  
        return 1

    c = n * factorial(n-1) 
    return c 

v = factorial(n)
print(v)



n1 = int(input("here number = "))
## 0,1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

def fibonacci(n1):
    if n1 == 0:
        return 0
    if  n1 == 1:
        return 1   

    b = fibonacci(n1-1) + fibonacci(n1-2)
    return b    

u = fibonacci(n1)   
print(u) 
'''
n2 = int(input("here number = "))

def dominoes(n2):
    if n2==0:
        return 1
    if  n2<0:
        return 0 

    b = dominoes(n2-1) + dominoes(n2-2) + dominoes(n2-3)
    return b    

uii = dominoes(n2)   
print(uii) 


