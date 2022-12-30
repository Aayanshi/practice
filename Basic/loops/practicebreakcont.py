# 0 to 10 print have to skip 5 or 11 hote hi break
i = 0
while(True) :
    
    if i+1 == 5:
        i = i + 1
        continue
    print("fuck off")
    if i + 1 > 10 :
         i = i + 1
         print("congo aapko")
         break


i = 0
#print(i)
while(True):
    i= i+1
    if i  == 5:
       
        continue
    print(i)
    if i+1>10:
        print("done")
        break


def number():
    n1=int(input("enter you first= "))
    n2=int(input("enter your last= "))
    for i in range(n1,n2+1):
        return(i)

bhaadmejao = number()   
print(bhaadmejao)



number()