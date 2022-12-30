
'''Solve following questions with the help of recursion:
Q-1 ) Check if a number is Palindrome: (5 marks)
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
n = input("here= ")
l = len(n)
c = ""
for i in range(l-1,-1,-1):
    c = c + n[i]
print(c)    
if n == c :
    print("yess")   
else:
    print("no") 
print(c)







