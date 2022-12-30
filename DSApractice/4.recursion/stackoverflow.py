# infinite loop
'''
def func1(i):
    if i == 1:      # we can`t use break as they use in loops , we use return to end a function
        return 2
    print(i)
    func1(i-1)



c = func1(7)
print(c)
print("stackoverflow")
'''

def fun1(i):
    a = 0

    if i == 100 :
        a = a+i
        
        return a
    fun1(i+1)    

r = fun1(5)  
print(r)
'''print(fun1()) ''' 






def factorial(n):
    if n == 1 :
        return 1
    p =( n*factorial(n-1))
    return p

if __name__ == "__main__":
    n = int(input("Enter your number = ")) 
    re = factorial(n)   
    print(re)    
