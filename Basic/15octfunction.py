# one liners 
# we can write if a<b : 


#there are two types of functoins
# built in 
# 2. user defined
def number():
    n1=int(input("enter you first= "))
    n2=int(input("enter your last= "))
    for i in range(n1,n2+1):
        return(i)

bhaadmejao = number()   
print(bhaadmejao)



def funk1():
    print("you can ")
funk1()    


def aaina():
    u = int(input("here= "))
    b = int(input("here= "))
    print(u + b,"ans.")

aaina() 

def aaina():
    u = int(input("here= "))
    b = int(input("here= "))
    print(u + b,"ans.")

aaina()

def func(a,b):
    print("kya", a + b)

print(func(1,2))    


def average():
    """ this is function for average"""    
    n1 = int(input("yahan= "))
    n2 = int(input("yahan bhi= "))
    av = (n1 + n2)/2
    return av


print(average())   
print(average.__doc__)



n = int(input("here= "))
ans = 0
for i in range(1,n+1):
    cube = (i ** 3)
    ans = cube + ans
print("answer=", ans)


n=9
for i in range(2,n+1): # eat 1 from end value starting value se no connection
    print(i)
 


# 10 1to15
n1 = 10
for i in range(5,16):
    table = n1 * i 
    print(table)    


n1 = 10
sum = 0
for i in range(1,11):
    table = n1 * i 
    sum = table + sum
    print(sum)    
       

n= "kub "
k = "aainu "
for i in range(0,5):
    l = n + "lobe "
    k = l + k
    print(k,i)