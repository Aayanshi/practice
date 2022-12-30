'''Q - 1) Write a program to print the sum of right diagonal of a matrix: (5
marks) Right diagonal is shown below:
[1 2 3
4 5 6
7 8 9]
 

[1 2 3 4
 5 6 7 8
 9 10 11 12]


[1 2
 3 4
 5 6]
'''
#ans.1
a = [
    #r0  1  2
    [1 ,2 ,3], #0col
    [4 ,5 ,6], #1
    [7 ,8 ,9]  #2
]

n = len(a)
m = len(a[0])
c = []

'''for i in range(3):
    c.append(a[i][3-i-1])
d = 0    
print(c,"right digonals") 
for i in c:
    d = i + d
print(f"here is sum of {a} matric is {d}")'''

sum = 0
for i in range(n):
    for j in range(m):
        if i + j == m-1:
            print(a[i][j])
            sum = sum + a[i][j]

print(f"here is sum of the anti digonals {sum}")            

#ans.2
b =[ 
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

n = len(b)
m = len(b[0])
sum = 0
for i in range(n):
    for i in range(m):
        if i + j == m-1:
            sum = sum + b[i][j]

print(f"here is sum of the anti digonals {sum}")            

 

#ans .3

c =[  #0 1 
     [1,2],
     [3,4],
     [5,6]
]

n = len(c)
m = len(c[0])
sum =0

for i in range(n):
    for j in range(m):
        if i+j == m-1:
            sum = sum + c[i][j]

print(sum)            
