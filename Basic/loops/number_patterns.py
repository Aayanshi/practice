# number patterns 
#1. increasing square
#simple method
n1 = int(input(" tell your no.= "))

for i in range(0,n1,1):
    for j in range(0,n1,1):
        print( "^" ,i ,end=" ")
    
    print()    

#counter method 
n1 = int(input(" tell your no.= "))
huh = 1
for i in range(0,n1,1):
    for j in range(0,n1,1):
        print(huh,end=" ")
    huh = huh + 1
    print()    



# decreasing square

# only counter method 
n1 = int(input(" tell your no.= "))
rev = n1                 # reverse or decrease no. squares me input will be the value of  counter variable 
for i in range(0,n1,1):
    for j in range(0,n1,1):
        print(rev ,end=" ")
    rev= rev - 1
    print()      


# increasing no.triangle  
n2 = int(input(" put your no. here= ")) 
tri = 1
for i in range(0,n2,1):
    for j in range(0,i+1,1):
        print(tri, end=" ")
    tri = tri +1
    print()        


# decreasing no. triangle
n2 = int(input(" put your no. here= "))
tri = n2
for i in range(0,n2,1):
    for j in range(0,i+1,1):
        print(tri, end=" ")
    tri = tri - 1
    print() 

n2 = int(input(" put your no. here= "))

for i in range(0,n2,1):
    for j in range(0,i+1,1):
        print(j, end=" ")
    
    print() 


n2 = int(input(" put your no. here= "))

for i in range(0,n2,1):
    w = n2
    for j in range(0,i+1,1):
        print(w, end=" ")
        w = w-1
    
    print() 

n2 = int(input(" put your no. here= "))

for i in range(0,n2,1):
    w = 1
    for j in range(0,i+1,1):
        print(w, end=" ")
        w = w + 1
    
    print() 

for i in range(6):
    for j in range(7):
        if (i==0 and j%3 !=0) or (i==1 and j%3 ==0) or (i-j==2) or (i+j==8):
            print("InU", end = "  ")
        else:
            print(" ", end = "   ")
    print("    ")

for i in range(6):
    for j in range(7):
        if (i==0 and j%3 !=0) or (i==1 and j%3 ==0) or (i-j==2) or (i+j==8):
            print("iloveu", end = "  ")
        else:
            print(" ", end = "   ")
    print("    ")    


    
