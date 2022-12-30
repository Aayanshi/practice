'''mat = [
    #r0 1 2
    [1,2,3], #col0
    [4,5,6], #1
    [7,8,9]  #2
]

print(mat[2][2])
n =len(mat)
m =len(mat[0])
print(f"n = {n}\nm = {m} ")

for i in range(n):
    for j in range(m):
        print(mat[i][j])
    print()    
      
      '''  #print(mat[0][j])

#squre matrix  
'''Q - 1) Write a program to print the sum of right diagonal of a matrix:'''

a = [ 

    [1,2,3,],
    [4,5,6,],
    [7,8,9 ]

]

n = len(a)
m = len(a[0])
s = 0
for i in range(n):
    s = s + a[i][n-i-1]
print(s)        


ab = [ 

    [1,2,3,4],
    [4,5,6,5],
    [7,8,9,7],
    [10,11,12,11]

]

n = len(ab)
m = len(ab[0])
sum = 0
for i in range(min(n,m)):
    sum = sum + ab[i][m-i-1]

print(sum)    

