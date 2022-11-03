print(" Good morning, lets calculate")

n1 = (int(input("your first number= ")))
n2 = (int(input("your second number= ")))

print("choose operation: \n1.Addition(+) \n2.Subtraction(-) \n3.multiplication(*) \n4.divission(/)")
opt = input("enter your operation here= ")
if opt == "+" :
    if n1 == 56 and n2 == 9 :
        print("result= 77")
    else :
        add = n1+n2
        print("result= ",add)
elif opt == "-" :
    sub = n1-n2
    print("result= ",sub)
elif opt == "*" :
    if  n1 == 45 and n2 == 3 :
        print("result= 555")
    else :
        mul = n1*n2
        print("reult= ",mul)
elif opt == "/" :
    if n1 == 56 and n2 == 6 :
        print("result= 4")
    else :
        div = n1/n2
        print("result= ",div)
else:
    print("beta padai vadai kar lo")

print("thankyou, have a good day")