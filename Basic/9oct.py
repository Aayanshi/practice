#break continue 
i = 0
while(i<45):
    print(i + 1, end= " ")
    if (i==44):
        break
    i = i + 1

# user se input lena ahi jab woh hundered se upar ho jaye toh break

i = 0
while(True) :
    n1 = int(input("your number please= "))
    if n1 < 100 :
        i = i + 1
        print("too low")
        continue
    elif n1 < 100 :
        i = i + 1
        print("got it right")
        break
     


while(True) :
    n1 = int(input("your number please= "))
    if n1 >100:
        print("right, got it")
        break
     
    else :
        print("too low")
        continue




str1 = "welovetocodetogether"
for i in str1:
    if i == "e":
        break
    print(i, end="")


    



     

