######### CC recursion1
'''Q-3  Reverse a string using recursion:(5 marks)
If we have a string, write a function that prints reverse of that string, using
recursion.
Sample Input:
ABCD
Sample Output:
DCBA'''

st = input("enter here= ")
def reversesting(st):
    l = len(st)
    if l == 0:
        return 
    
    reversesting(st[1:])
    q = st[0]
    print(q)


ans = reversesting(st)    
print(ans)