#function cc
'''1. def printMax(a, b):
2. if a > b:
3. print(a, 'is maximum')
4. elif a == b:
5. print(a, 'is equal to', b)
6. else:
7. print(b, 'is maximum')
8. printMax(3, 4)'''

# answer 1.
def max(a,b):
    if a > b :
        print(a, "its max")
    elif a == b :
        print(a, "is equal to",b)
    else:
        print(b,"its max")

max(3,4)            

'''def func(x):
3. print('x is', x)
4. x = 2
5. print('Changed local x to', x)
6. func(x)
7. print('x is now', x)'''


# answer 2.
def func(x):
    print("x is=",x)
        
x = 2
print("changed local variable x",x)
func(6) 
print("x is now", x)       


# answer 3.
def vowel():
    name =str(input("name here= "))
    for i in name:
        if i == "a" or i== "A" or i == "i" or i == "e" or i == "o" or i == "u":
            continue
        else :
            print(i,end="")    

vowel()

print()

def name():
    n = str(input("name =  "))
    for i in n :
        if i == "t" or i == "p" or i == "a"or i == "k":
            continue
        else:
            print(i, end="")

name()

def vow():
    f = str(input("naam likh= "))

    for i in f :
        if i == "A" or i == "a" or i == "E" or i == "e" or i == "O" or i == "o" or i == "U" or i == "u":
            continue 
        
        else:
            print(i,end="",)
            


vow()
