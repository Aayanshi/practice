'''n = int(input("here= "))
x = 5
for i in range(x):                    
    print(n)'''

'''Q-2 ) Program for Sum of the digits of a given number:(5 marks)
Sample Input:
1234567
Sample output:
28
'''

''' q2Given an integer, write a function that returns true if the given number is
palindrome, else false.
For example,
Sample input:
12321
Sample output:
palindrome
'''


def sumdigt(num,x):
    if num == 0:
        return x
    x = x + num % 10
    return sumdigt(num // 10,x)

''''
def palindrome(num,y):
    if num == 0 :
        return y
    y = y * 10 + num % 10
    return palindrome(num // 10,y)

if __name__ == "__main__":
   num = int(input("here= "))

   ## sum of digits
   res = sumdigt(num,0)
   print(res)

   ## palindrome
   ans = palindrome(num,0) 
   print(ans)
   if ans == num :
    print("Yes, its palindrome")
   else:
    print("Oops not its not...") '''


'''Q-3 ) Given a number n, find sum of first n natural numbers:(5 marks)
Examples :
Input : 5
Output : 15
Explanation : 1 + 2 + 3 + 4 + 5 = 15
Input : 7
Output : 28
Explanation : 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28'''

## iterative

'''n = int(input("number here= "))

b = 0
for i in range(1,n+1):
    b = b + i
print(b)  

  
def naturalsum(n,z):
    if n == 1:
        return z
    z = z + n 
    return naturalsum(n-1,z)    

out = naturalsum(n,1)
print(out)    '''


'''Q-4 ) [Bonus Question] Given two number x and y, find product using
recursion.
(3 extra marks)
Examples :
Input : x = 5, y = 2
Output : 10'''


## interative
n = int(input("number 1= "))
m = int(input("number 2= "))
print(n * m)

def product(n,m,o):
    if m == 0:
        return o
    o = o + n
    return product(n,m-1,o)   

c = product(n,m,0)

