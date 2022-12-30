# fibonacci series
n = int(input("enter number= "))
def fibonacci(n):
    if n == 1 :
        return 1
    if n == 0:
        return 0    
    else:
        return fibonacci(n-1) + fibonacci(n-2)    


# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 

ans = fibonacci(n)
print(ans)