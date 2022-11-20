#functions with parameters

def cube():
    s = int(input("here= "))
    q = 0
    for i in range(1,s+1):
        p = i **3
        q = q + p
    print(q)

cube()

def add(a,b): #a,b are parameters or arguments here we input
    s = a+b
    return(s)  # here return has stored the answer as output

#there are two ways of printing function values
re = add(12,2) #1. putting into any variable and print them
print(re)

print(add(12,2)) #2. or we simply print that func. with parameters


# star function

def star(n):
    
    for i in range(1,n+1):
        for j in range(i):
            print("@", end=" ")
            
        print( )        

n = int(input("here= "))
star(n)

def test(n):
    for i in range(n,1,-1):
        print(i)
        break
    print(0)

test(10)

def line(n):
    for i in range(1,n+1):
        print("*  "*i)

line(4)  



def scope():
    s = 10
    for i in range(10):
        s = 0
    print(s)    

scope()