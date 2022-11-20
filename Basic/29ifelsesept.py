#harry if else
var1 = 45
var2 = 33
var3 = (int(input("here= ")))

if var1 > var3 :
    print("greater")
if var1 == var3 :
    print("equal")    
if var1 < var3 :
    print("smaller") 
    

list = [1,2,3,4,5,22,45,67]
if 7 not in list :
    print("wrong answer")

list = [1,2,3,4,5,22,45,67]
if 2 in list :
    print("right answer")  
elif 6 in list :
    print("wrong answer")


print("driving staus")          
age = (int(input("write your age= ")))  
if age > 18 :
    print("you can drive")
elif age < 18 :
     print("you cant drive")
elif age == 18 :
    print("meet physicaaly")
else:
    print("do your own bussiness")    


print("driving staus")          
age = (int(input("write your age= ")))  
if 18<age<90 :
    print("you can drive")
elif age == 18 :
    print("meet physicaaly")
else:
    print("do your own bussiness")    

a = 23
b = 56
if a>b :
    print("smaller")
elif a<b:
    print("bigger")    
