'''Week 3- Day 3 : Coding Challenge
(Maximum marks -15)
Q1. Write a program to take input from the user and make a list of integers
(Easy) (5 marks)
Input:
8
5
5
6
7
8
Output:
[8,5,5,6,7,8]
Q2. Write a program to convert above list to a tuple
. (Easy) (5 marks) Input: [8,5,5,6,7,8]
Output: (8,5,5,6,7,8)
Q3. Write a program to remove the 4th last element from a list, and put a
string before the 2nd last element (Medium) (5 marks)
Input:
Any list, lets say [1,2,3,4,5,6,7,8,9]
Output:
[1,2,3,4,5,7,hello,8,9]'''

'''#1.
n = int(input(" enter your number=  "))
l = []
l.append(n)
print(l)


#2.
a =[8,5,5,6,7,8]
print(tuple(a))

#3.
p=[1,2,3,4,5,6,7,8,9]
p.remove(6)
p.insert(-2,"hello")
print(p)


n = 6 
drew= []
for i in range(n+1):
    res = int(input("enter the numbers one by one  "))
    drew.append(res) 
print(drew)'''

# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	ele = int(input())

	lst.append(ele) # adding the element
	
print(lst)

