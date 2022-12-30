####### ccc 1 rec
'''Q-2 ) Write a function that prints digits of a number from left to right , using
recursion:(5 marks)
Sample Input:
1234567
Sample output:
1
2
3
4
5
6
7'''

### itriate

'''n = (input("here= ")) #123
for i in n:          
    c = int(i) % 10 #1 
    print(c)  
'''
#### rec

def digits(di):
    if  di == 0 :
        return  
    c = digits(di// 10)
    print(di % 10)      


if __name__ == "__main__":
    di = int(input("Enter number= "))
    digits(di)
    

''' Reverse a string using recursion:(5 marks)
If we have a string, write a function that prints reverse of that string, using
recursion.
Sample Input:
ABCD
Sample Output:
DCBA
'''

'''n = input("enter here= ")

def reverse(n):
    l = len(n)
    if l == 0:
        return 
    b = n[0]
    reverse(n[1:])
    print(b)    

reverse(n)
'''


'''Q-2 ) Program for Sum of the digits of a given number:(5 marks)
Sample Input:
1234567
Sample output:
28
'''
'''
## iterative
p = (input("here = "))
l = len(p)
sum = 0
for i in p:
    sum = sum + int(i)
print(sum)    


## rec
p = int(input("here number= "))

def sumdigits(p,x):
    if p == 0 :
        return x
    x = x + p % 10    
    return sumdigits(p//10,x)
    
ver = sumdigits(p,0) 
print(ver)


'''

'''Q-1 ) Check if a number is Palindrome: (5 marks)
Given an integer, write a function that returns true if the given number is
palindrome, else false.
For example,
Sample input:
12321
Sample output:
palindrome
eg2:
Sample input:
1451
Sample output:
not palindrome.
'''


###iterative
'''
n = input("here your number= ")
l = len(n)
v = ""
for i in range(l-1,-1,-1):
    v = v + n[i]
print(v)
if v == n :
    print("palli yes")
else :
    print("no")   

num = int(input("here= "))

st = str(n)
bst = st[::-1]
if st == bst:
    print(True)
else:
    print(False)

### rec'''
'''
def pallindrome(num,x):
    
    if num == 0:
        return x
    x = x * 10 + num % 10
    return pallindrome(num//10,x)


if __name__ == "__main__":       
    num = int(input("here= "))
    re = pallindrome(num,0)
    print(re)
    if re == num :
        print("palindrome")
    else :
        print("not palindrome")    '''



