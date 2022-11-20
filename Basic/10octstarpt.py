#star pattern practice
n = int(input("how many Inu you want in each side of your starredsquare =  "))
for i in range(n):
    for j in range(n):
        print("Inu", end=" ")
    print()       
    #to make square we simply multiply ranges of i and j range its by default they multiply each other 


n1 = int(input("tell your hashcount= "))
for i in range(0,n1,1):
    for j in range(0,n1,1):
        print("#", end="       ") 
    print()  
# to make rectangle we need more horizontal spaces we increse space btw end=" "
# to make rect or horizontal spaces u use end=" " the space btw the end gives broader look
# to make square or vertical spces u use print( ) this is work as new line character \n as well as difference/skip also make vertical space


n2 = int(input("tell your hashcount= "))
for i in range(0,n2,1):
    for j in range(0,i+1,1):
        print("#", end=" ") 
    print()  
    
# to make increasing triangle we use j range(0,i+1,1) cause here i+1 predecessor the value of n1

n2 = int(input("tell your hashcount= "))
for i in range(0,n2,1):
    for j in range(i,n2,1):
        print("#", end=" ") 
    print() 
# to make decresing triangle we use j range (i,n2,1)here we play with starting value and i will change acc to first for statement 


n3 = int(input("put your number= "))
for i in range(0,n3-1,1):
    for j in range(0,i+1,1):
        print("@", end=" ")
    print( )  
for i in range(0,n3,1):
    for j in range(i,n3,1):
        print("@" , end=" ")
    print( )
#for making left side arrow head shape|> we use above code, and for pointed shaped we use i range(upar wali range) 0, n1-1,1 


n4 = int(input("put your number= "))
for i in range(0,n4,1):
    for j in range(i,n4,1):
        print(" " , end=" ")
    for j in range(0,i+1,1):
        print("*", end=" ")    
    print( )
#to make increasing rignt triangle we use three loops and j is twice last j range(0,i+1,1)


n5 = int(input("put your number= "))
for i in range(0,n5-1,1):
    for j in range(i,n5,1):
        print(" " , end=" ")
    for j in range(0,i+1,1):
        print("*", end=" ") 
    print( )    
for i in range(0,n5,1):
    for j in range(0,i+1,1):
        print(" ", end=" ")
    for j in range(i,n5,1):
        print("$" , end=" ")
    print( ) 


   

