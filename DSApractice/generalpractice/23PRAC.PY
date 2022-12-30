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
not palindrome.'''

n = input("= ")

l = len(n)
p = "" 
for i in range(l-1,-1,-1):
    p = p + n[i]
print(p)    
if n == p:
    print("yes")



num = int(input("here= "))

def pali(num,b):
    if num == 0:
        return b
    b = b * 10 + num % 10
    return pali(num//10,b)  

re = pali(num,0)
print(re)

'''Q-2 Program for Sum of the digits of a given number:(5 marks)
Sample Input:
1234567
Sample output:
28'''