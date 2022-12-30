#matrics

'''mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
n = len(mat)
m = len(mat[0])
print(f" dimension {n} x {m}")

for i in range(n):
    for j in range(m):
        print(mat[i][j], end=" ")
    print()        

print()

for i in range(n):
    print(mat[i][i])'''

'''print()

for i in range(m):
    print(mat[i][n-i-1])    

print()

for i in range(n):
    for j in range(m):
        print(mat[i][2])




## fromuser matrix
matrix = [ ]
n = int(input("enter your row number= "))
m = int(input("enter your column number= "))
e = int(input("no . of elements= "))
print(f" dimension {n} x {m}")

for i in range(n):
    matrix.append([])
    for j in range(m):
        c = int(input("enter your elements= "))
        matrix[i].append(mat)

print(matrix)        

a = [[e for j in range(m)] for i in range(n)]
print(a)

'''


##### sum of right digonals

'''v = [#0 1 2 
    [1,2,3], #0
    [4,5,6], #1
    [7,8,9]  #2
]

n = len(v)
m = len(v[0])
sum = 0

for i in range(n):
    for j in range(m):
        if i + j == m - 1:
            sum = sum + v[i][j]

print(sum)         


x = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
] 
 
n = len(x)
m = len(x[0])
print(f" dimension {n} x {m}")
sum = 0


for i in range(n):
    for j in range(m):
        sum = sum + x[i][j]

print(sum)


z = [
    [1,2],
    [3,4],
    [5,6] 
]

n = len(z)
m = len(z[0])
sum = 0


for i in range(n):
    for j in range(m):
        sum = sum + z[i][j]

print(sum)'''


###### sum of borders cc

'''Border elements:
1 2 3 4
4 5 6 5
7 8 9 6
4 9 8 7
Sum of border elements = 1+2+3+4+5+6+7+8+9+4+7+4 = 60'''

'''bor = [
    #0 1 2 3
    [1,2,3,4], #0
    [4,5,6,5], #1
    [7,8,9,6], #2
    [4,9,8,7]  #3
]

n = len(bor)
m = len(bor[0])
print(f"size = {n} x {m}")
sum = 0

for i in range(n):
    for j in range(m):
        if i == 0 :
            sum = sum + bor[i][j] 

        elif j == 3: # j == m-1
            sum = sum + bor[i][j]

        elif i == 3 : # i == n-1
            sum = sum + bor[i][j]

        elif j == 0 : 
            sum = sum + bor[i][j]

print(sum)                    
'''

### sum of rows n columns 

'''Q - 3) Write a function to return sum of rows of a matrix as a list: (5 marks)
Sample Input:
This matrix :
1 2 3 4      0
5 6 7 8      1
9 10 11 12   2
13 14 15 16  3
Sample output
should return,
10
26
42
58'''

def sumrows(fuc):     
    n = len(fuc)
    m = len(fuc[0])
    print(f" {n} x {m} dimension")
    
    
    l = [ ]
    for i in range(n):
        sum = 0
        for j in range(m):
        
            if i == 0 :
                sum = sum + fuc[i][j]
                
            
            elif i == 1 :
                sum = sum + fuc[i][j]
                

            elif i == 2 :
                sum = sum + fuc[i][j]
                

            elif i == n-1 :
                sum = sum + fuc[i][j]
        
        l.append(sum)                   
    
    print(l)


fuc = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ] 

sumrows(fuc)
    

####### his way  
m = len(fuc)
n = len(fuc[0])
listrowsum = []
for i in range(m):
    sumrow = 0
    for j in range(n):
        sumrow = sumrow + fuc[i][j]
    listrowsum.append(sumrow)
print(listrowsum)


#print sum of columns as list(sum of each column as an element)
m = len(fuc)
n = len(fuc[0])
listcolsum = []
for i in range(m):
    sumcol = 0
    for j in range(n):
        sumcol = sumcol + fuc[j][i]
    listcolsum.append(sumcol)
print(listcolsum)
     

