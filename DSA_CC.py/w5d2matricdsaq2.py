'''Q - 2) Write a program to print sum of border elements of a square Matrix
(5 marks)
Border elements:
1 2 3 4
4 5 6 5
7 8 9 6
4 9 8 7
Sum of border elements = 1+2+3+4+5+6+7+8+9+4+7+4 = 60'''

'''l= [ 
    #0 1 2 3
    [1,2,3,4], #0
    [4,5,6,5], #1
    [7,8,9,6], #2
    [4,9,8,7]  #3

]

n = len(l)
m = len(l[0])
c = 0
print(n,"x",m)
for i in range(n):
    for j in range(m):
        if i == 0:
            c = c+l[i][j]
        elif j == m-1:
            c = c+l[i][j]
        elif i == n-1:
            c = c+l[i][j]
        elif j == 0:
            c = c+l[i][j]
        else:
            c = c+0

 
print(c)'''
    



'''Q - 3) Write a function to return sum of rows of a matrix as a list: (5 marks)
Sample Input:
This matrix :
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
Sample output
should return,
[10
26
42
58]'''
#an3.

s = [ 
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]

]

n = len(s)
c = [ ]
r = 0
'''for i in range(n):
    c.append(sum(s[0][i]))
   r = r +i'''


for i in range(n):
    c.append(s[1][i])

for i in range(n):
    c.append(s[2][i])   

for i in range(n):
    c.append(s[3][i])      
   
print(c) 
bc = 0
for i in c:
    bc = bc + i 

print(bc)    


