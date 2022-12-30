'''Q - 3 ) Check If N and Its Double Exist:
https://leetcode.com/problems/check-if-n-and-its-double-exist/
Given an array arr of integers, check if there exists two integers N and M such
that N is the double of M ( i.e. N = 2 * M).
More formally check if there exists two indices i and j such that :
● i != j
● 0 <= i, j < arr.length
● arr[i] == 2 * arr[j]
Example :
Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5'''

'''
l = [2,3,7,8,14,4,16]
n = len(l)

for i in range(n):
    m = i
    if i == 2 * m or n != m:
        print("true")
        
    else :
        print("false")
        '''
   
'''
l = [2,3,5,9,11,13]   
n = len(l)
m = False
for i in range(n):
    for j in range(1,n):
        if l[i] == 2 * l[j] :
            m = True
        else :
            continue    
print(m)
'''



'''Q - 1) Write a program to print the sum of right diagonal of a matrix: (5
marks) Right diagonal is shown below:
1 2 3
4 5 6
7 8 9

1 2 3 4
5 6 7 8
9 10 11 12

1 2
3 4
5 6'''

a = [ 
    #0 1 2 col
    [1,2,3], #0
    [4,5,6],#1
    [7,8,9] #2 row
]

n = len(a)
m = len(a[0])
print(f"this matrix of {n} x {m}")
s = 0

for i in range(n):
    for j in range(m):
        if (i+j) == m-1:
            s = s +(a[i][j])

print(s)        


b = [ 

    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12] 
]

n = len(b)
m = len(b[0])
s = 0

for i in range(n):
    for j in range(m):
        if (i+j) == m -1 :
            s = s + (b[i][j])

print(s)


bc = [ 
    
    [1,2],
    [3,4],
    [5,6]
]


n = len(bc)
m = len(bc[0])
s = 0
for i in range(n):
    for j in range(m):
        if (i+j) == m - 1:
            s = s + (bc[i][j])

print(s)            
