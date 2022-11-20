# horizontal are rows "i"  right left peek 
# vertical are columns "j" up down peek 


#square
n = int(input("put your number= "))
for i in range(n):  
    for j in range(n):
        print("^", end=" ")
    print()


#rectangle
n1 = int(input("put your number= "))
for i in range(n1):
    for j in range(n1):
        print("!", end="  ")
    print( )        

#left increasing triangle
n2 = int(input("put your number= "))
for i in range(0,n2,1):
    for j in range(0,i+1,1):
        print("&", end=" ")
    print()

#left decreasing triangle
n3 = int(input("put your number= "))
for i in range(0,n3,1):
    for j in range(i,n3,1):
        print("*", end=" ")
    print()

#left arrow head
n4 = int(input("put your here= "))
for i in range(0,n4-1,1):
    for j in range(0,i+1,1):
        print("~", end=" ")
    print()    
for i in range(0,n4,1):
    for j in range(i,n4,1):
        print("~",end=" ")
    print()            

#right increasing tiangle
n5 = int(input("put your number= "))
for i in range(0,n5,1):
    for j in range(i,n5,1):
        print(" ",end=" ")
    for j in range(0,i+1,1):
        print("*",end=" ")
    print()

#right decreasing triangle
n6 = int(input("put your number here= "))
for i in range(0,n6,1):
    for j in range(0,i+1,1):
        print(" ", end=" ")
    for j in range(i,n6,1):
        print("%",end=" ")
    print()        


'''#right arrow head
n7 = int(input("put your number= "))
for i in range(0,n7-1,1):
    for j in range(i,n7,1):
        print(" ", end=" ")
    for j in range(0,i+1,1):
        print("-", end=" ")
    print()
for i in range(0,n7,1):
    for j in range(0,i+1,1):
        print(" ", end=" ")
    for j in range(i,n7,1):
        print("-",end=" ")
    print()               
    # emptyprint sirf do baar hi aayega 
'''


'''#piramid
n8 = int(input("put your number= "))
for i in range(0,n8,1):
    for j in range(i,n8,1):
        print(" ", end=" ")
    for j in range(0,i,1):
        print("*" , end=" ")
    for j in range(0,i+1,1):
        print("*", end=" ")
    for j in range(i,n8,1):
        print(" ", end=" ")
    print()            
#to make peak in this we want to remove one extra line so i+1 ki jagah sirf i likhegey 

#reverse pyramid
n9 = int(input("put your number= "))
for i in range(0,n9,1):
    for j in range(0,i+1,1):
        print(" ",end=" ")
    for j in range(i,n9-1,1):
        print("^", end=" ")
    for j in range(i,n9,1):
        print("^", end=" ")
    for j in range(0,i+1,1):
        print(" ",end=" ")
    print()    '''
# to make peek in reverse pyramid we gonna -1 into any n9 from j ;oop to reduce one line

#dimond
n0 = int(input("put your number= "))
for i in range(0,n0,1):
    for j in range(i,n0,1):
        print(" ",end=" ")
    for j in range(0,i,1):
        print("*",end=" ")
    for j in range(0,i+1,1):
        print("*",end=" ")
    for j in range(i,n0,1):
        print(" ",end=" ")  
    print()
for i in range(0,n0,1):
    for j in range(i,n0,1):
        print(" ",end=" ")
    for j in range(0,i,1):
        print("*",end=" ")
    for j in range(0,i+1,1):
        print("*",end=" ")
    for j in range(i,n0,1):
        print(" ",end=" ")          
    print() 


n0 = int(input("put your number= "))
for i in range(0,n0-1,1):
    for j in range(i,n0,1):
        print(" ",end=" ")
    for j in range(0,i,1):
        print("*",end=" ")
    for j in range(0,i+1,1):
        print("*",end=" ")
    for j in range(i,n0,1):
        print(" ",end=" ") 
    print()     
for i in range(0,n0,1):
    for j in range(0,i+1,1):
        print(" ",end=" ")
    for j in range(i,n0-1,1):
        print("*",end=" ")
    for j in range(i,n0,1):
        print("*",end=" ")
    for j in range(0,i+1,1):
        print(" ",end=" ")          
    print()    