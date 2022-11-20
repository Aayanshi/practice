#While loop

i = 2
while (i<20):
    print(i + 3)
    i = i+ 3


i = 1
while (i<27):
    print(i)
    #isme aapne ladai ki thi
    

i = 2
while (i<=2):
    n1 = int(input("enter your no.- "))
    
    
    if n1 % 3 ==0 and n1 % 5 == 0:
        print("fizz-Buzz")
        continue
    elif n1 % 3 == 0:
        print("fizz")
        continue
    elif n1 % 5 == 0 :
        print("fuzz")
        continue
    else :
        print("beta tumse na ho paayega")
        continue 


i = 1
while i < 6 :
    print("u")
    i = i +1
