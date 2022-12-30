### recursion w6d1 cc 



''' q1Write a function that prints digits of a number from left to right , using
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

##iterative way
n =(input("enter here= ")) # 1234
c = len(n)                # 3
for i in range(c-1,-1,-1):
    print(int(n[i]))

## modulus iterative way
for i in str(n):
    b = int(i) % 10
    print(b)


## recursion
numb = 123

def digits(numb):
    if numb == 0 :
        return 
    v = digits(numb//10)
    print(numb % 10)
    
digits(numb)



''' q2 Reverse a string using recursion:(5 marks)
If we have a string, write a function that prints reverse of that string, using
recursion.
Sample Input:
ABCD
Sample Output:
DCBA'''
  


a = input("here= ")
s = len(a)
## iterative way
for i in range(s-1,-1,-1):
    print(a[i],end="")

## recursion way
def stingreverse(a):
    l = len(a)
    if l == 0 :
        return 

    c = a[0]
    stingreverse(a[1:])
    print(c,end="")

stingreverse(a)








 



