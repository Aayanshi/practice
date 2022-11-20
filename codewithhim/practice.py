
'''Take an integer number as input and print its last digit. 
input: 
123456 
output: 
6'''
#ans
def output():
    n =int(input("your number please= "))
    p = str(n)
    return(p[-1])

c = int(output())
print(c)

'''Write a program to find the factorial of a number. 
(Easy) (3.75 marks) 
input: 
5'''

#ans
c = 1
n = int(input("your number= "))
for i in range(1,n+1): # multiplication me nevr take zero
    c =(c*i) 
print(c)

#class circle me jao
r = int(input("input radius= "))
a = 3.14 * r * r  
print("here is area of circle =" , a )  