'''ew = [ 
      
    [0,1,0],
    [1,0,1],
    [0,1,0]

]
n = 3
A = []
for i in range(n):
    A.append([])
    for j in range(n):
        A[i].append(0)
print(A)


# to make matrix from user 
# way one
matrix = []
n = int(input("enter your row= "))
m = int(input("enter your column= "))
print(f"Order of matrix will be {n} x {m}")

for i in range(n):
    matrix.append([])
    for j in range(m):
        mat = int(input(f"enter your element for your matrix {i+1} and {j+1} = "))
        matrix[i].append(mat)

print(matrix)        

#2 way two by list comperehension method
n =int(input("enter here row="))
m = int(input("enter your col="))
s = int(input("enter your element= "))
matrix =[ [s for j in range(m)] for i in range(n)   ]
print(matrix)
'''

matrix =[

    [1,2,3], 
    [4,5,6], 
    [7,8,9]
]

n = len(matrix)
m = len(matrix[0])

for i in range(n):
    for j in range(m):
        print(matrix[j][i], end=" ")
    print()    





