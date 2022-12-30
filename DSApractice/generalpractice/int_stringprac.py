# cc
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
7
'''

# iterative
'''n = 123566
for i in range(len(n)):
    c = int(n[i]) % 10
    print(c)  '''  

def sting(n):
    if n == 0 :
        return 
    c = sting(n//10)
    return (n % 10)    



if __name__ == "__main__":
    n = int(input("enter= "))
    re = sting(n)
    print(re)


'''Q-3 ) Reverse a string using recursion:(5 marks)
If we have a string, write a function that prints reverse of that string, using
recursion.
Sample Input:
ABCD
Sample Output:
DCBA
'''

