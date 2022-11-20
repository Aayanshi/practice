'''Write a Python program which accepts the user's first and last name and 
print them in reverse order with a space between them'''
n = input("first namme=")
p = input("last name=")
print(p, n)

'''Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')'''

l = []
for i in range(0,6):
    n = int(input(" your numbers= "))
    l.append(n)
    
print(l)
t = tuple(l)
print(t)

'''Write a Python program to display the first and last colors from the following list. Go to the editor
color_list = ["Red","Green","White" ,"Black"]'''
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0:5:3])


'''Write a Python program to get the difference between a given number and 17,
 if the number is greater than 17 return double the absolute difference.'''
def difference():
    n = int(input("your number= "))
    if n > 17 :
        c = n- 17
        d = c * 2
        print(d)

    elif n <= 17:
        f = 17 - n 
        print(f)


difference()        

'''Write a Python program to test whether a number is within 100 of 1000 or 2000. Go to the editor
Click me to see the sample solution

18.

19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged. Go to the editor
Click me to see the sample solution

20. Write a Python program to get a string which is n (non-negative integer) copies of a given string. Go to the editor'''

n = int(input("your number greater than 100= "))
if n > 100 and n <= 1000:
    print("its in range of 100 to 1000")

elif n > 1000 and n <= 2000:
    print("its in range 1000 to 2000")   

else:
    print("its out from 2000 range")    



''' Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum. Go to the editor
Click me to see the sample solution'''    
n = int(input("enter first number= "))
p = int(input("enter your second number= "))
j = int(input("enter your third number= "))
