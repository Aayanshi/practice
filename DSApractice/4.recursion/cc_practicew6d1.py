''''Q-2 ) Write a function that prints digits of a number from left to right , 
using recursion:(5 marks)
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
num = 22435627272282
bum = str(num)

'''li = len(bum)
for i in range(li):
    print(bum[i])
'''

for i in bum:
    print(int(i))

#print(li)
#while num != 0:
    
#itrative way

n = str(5673829)
def LeftRight(n):
    for i in n:
        print(int(i))        


LeftRight(n)




'''


n = int(2345)
for i in range(n):
    print(i)

n = input("enter here = ")
for i in range(len(n)):
    print(i)
'''