'''Q - 2) Write a program to print sum of border elements of a square Matrix
(5 marks)
Border elements:
1 2 3 4
4 5 6 5
7 8 9 6
4 9 8 7
Sum of border elements = 1+2+3+4+5+6+7+8+9+4+7+4 = 60
Q - 3) Write a function to ret'''

mtx =[ 
    #0 1 2 3
    [1,2,3,4],#0
    [4,5,6,5],
    [7,8,9,6],
    [4,9,8,7] #3
    
    ]

#sum of borders
n = len(mtx)
m = len(mtx[0])
'''c = 0

for i in range(n):
    for j in range(m):
        if i == 0:
            c = c + mtx[i][j]        
        
        elif j == 3  :
            c = c + mtx[i][j]

        elif i == 3:
            c = c + mtx[i][j]

        elif j == 0:
            c = c + mtx[i][j]

        else:
            c = c + 0

print(f"{c} is sum of rows")'''

k = 0
for i in range(n):
    for j in range(m):
        if j == 0:
            k = k + mtx[j][i]

        elif j == 1:
            k = k + mtx[j][i]

        elif j == 2:
            k = k + mtx[j][i]       

        elif j == 3:
            k = k + mtx[j][i]


print(k)


'''1 2 3 4
  5 6 7 8
  9 10 11 12
  13 14 15 16
  
  
  Write a function to return sum of rows of a matrix as a list: (5 marks)
  10
  26
  42
  58'''

kiki =[  
        
        [1,2,3,4]
        [5,6,7,8]
        [9,10,11,12]
        [13,14,15,16]
]
n = len(kiki)
m = len(kiki)
b = 0
for i in range(n):
    for j in range(m):
        print()
