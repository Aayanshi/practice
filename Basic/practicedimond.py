#love  u diamond
#hint = divide n draw



n = int(input("put your number= "))
for i in range(0,n-1,1):
    for j in range(i,n,1):
        print(" ", end=" ")
    for j in range(0,i,1):
        print("*",end=" ")
    for j in range(0,i+1,1):
        print("*" ,end=" ")
    for j in range(i,n,1):
        print(" ", end=" ")
    print()
for i in range(0,n,1):
    for j in range(0,i+1,1):
        print(" ", end=" ")
    for j in range(i,n-1,1):
        print("*", end=" ")
    for j in range(i,n,1):
        print("*",end=" ")
    for j in range(0,i+1,1):
        print(" ", end=" ")
    print()                         

# time model
n1 = int(input("put your number= "))
for i in range(0,n1-1,1):
    for j in range(0,i+1,1):
        print(" ", end=" ")
    for j in range(i,n1-1,1):
        print("*", end=" ")
    for j in range(i,n1,1):
        print("*",end=" ")
    for j in range(0,i+1,1):
        print(" ", end=" ")
    print()
for i in range(0,n1,1):
    for j in range(i,n1,1):
        print(" ", end=" ") 
    for j in range(0,i,1):
        print("*", end=" ")
    for j in range(0,i+1,1):
        print("*" , end=" ")
    for j in range(i,n1,1):
        print(" ",end=" ")
    print()                       

