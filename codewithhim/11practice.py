'''q1.calculate sum of all numbers from one to the input given by the user
'''
s = 0
n = int(input("your number = ")) 
for i in range(1,n+1):
    s = i + s 
print(s)  

#input by user of list
n = int(input("how many numbers you want in list = "))
curls = []
for i in range(n):
    curls.append(int(input()))

sum = 0
for i in curls:
    sum = sum+i
print(curls)
print(sum)

'''q2.write a program to find the factorial of a number given by the user
'''
k = 1
n = int(input("your number for factorial= ")) 
for i in range(1,n+1):
    k = i * k 
print(k)    

'''q3. Reverse an integer number given by the user
'''
n = int(input("Your number(min-two digits)= "))
s = str(n)
p = s[-1::-1]
q = int(p)
print(q)
print(type(q))


'''Use a loop to display elements from a given list present at odd index positions
'''
l = ["aaina","inu","pari",17,"lotus","kuber",62,96,"no"]
for i in range(len(l)):
    if i % 2 == 0 :
        print(l[i], ",", end="")


