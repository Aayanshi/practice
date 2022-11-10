#lets do assignment1
n1 = int(input("enter your first number= "))
n2 = int(input("enter your second number= "))
n3 = int(input("enter your third number= "))
if n1 > n2:
    if n2 > n1:
        print(n1,"this is bigger")
    print(n2,"this is bigger")   
else:
    n2 > n3 
    print(n2,"this is bigger")     
    if n3 > n2  :
        print(n3,"this is bigger")

n1 = int(input("enter your first number= "))
n2 = int(input("enter your second number= "))
n3 = int(input("enter your third number= "))
if n1 > n2 and n1 > n3:
    print(n1,"this is bigger")
elif n2 > n1 and n2 > n3:    
    print(n2,"this is bigger")   
else: 
    print(n3,"this is bigger")


'''Q-3) FizzBuzz - if a number is divisible by 3 - print Fizz, if a number is
divisible by 5 - print Fuzz,if a number is divisible by both - print
Fizz-Buzz
                                                     (5 marks)
                                                     (Easy)
'''

   
#to print it as it is
for i in "aaina":
    print(i,end="")

#for sum of a list
curls = [23,34,45678,45,76,69,23]

sum = 0
for i in curls:
    sum = sum+i
print(sum)

#more complex sum of list inputed by user
n = int(input("how many numbers you want in list = "))
curls = []
for i in range(n):
    curls.append(int(input()))

sum = 0
for i in curls:
    sum = sum+i
print(curls)
print(sum)
