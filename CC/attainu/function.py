'''1. def printMax(a, b):
2. if a > b:
3. print(a, 'is maximum')
4. elif a == b:
5. print(a, 'is equal to', b)
6. else:
7. print(b, 'is maximum')
8. printMax(3, 4)
'''

'''Write a function which will take a str as input and will return a string
where vowels are removed. (Medium) (5 marks) Str = ABCDEFG
Result = BCDFG
'''
n = input("Enter Your Name= ")
p = []
def vowel(n):
    for i in n :
        if i == "A" or i == "E" or i == "O" or i == "I" or i == "U":
            p = [i]
            
        else:
            return 
          
        
re = vowel(n)   
print(re)     


'''2. def func(x):
3. print('x is', x)
4. x = 2
5. print('Changed local x to', x)
6. func(x)
7. print('x is now', x)'''

def func(x):
    print('x is', x)

x = 2
print('Changed local x to', x)
 
func(x)
print('x is now', x )


'''Write a function to print the reverse of a list, pass the list as a
parameter'''

num = [1,2,3,4,4,5,6,7,8,9,10,21,67,89]
def reversee(num):
    c = sorted(num)
    d = c.reverse(d)
    print(d)

v = reversee(num)
print(v)    

