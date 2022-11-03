# dict
'''Q1. Write a program to find the count of all even nos and odd nos in an
array / list
Eg
Input:
[1,2,3,4,5,6,7,8,9,10]
output:
Odd_count = 5
Even_count = 5 (Easy) (5 marks)'''


l = [2,3,6,4,1,7,20,10]
e = 0
p = 0
for i in l:
    if i % 2 == 0 :
        e = e + 1
    else :
        p = p + 1

print(p,"odd numbers")       
print(e ,"even numbers")


'''Q2. Write a program to create a dictionary for above program'''


l = [2,3,6,4,1,7,20,10]
e = 0
p = 0
d = { }
for i in l:
    if i % 2 == 0 :
        e = e + 1
        d["even numbers"] = e
    else :
        p = p + 1
        d["odd numbers"] = p

print(d)     

'''Q3. Write a program to find the count of every vowel in a string
eg.
Input:
envelope
Output :
{
A : 0,
E : 3,
I : 0,
O: 1,
U:0
}
'''
n = input("your name= ")
a = { }
b = 0
for i in n :
    if i == "a" or i == "e" or i == "o" or i == "u" or i == "i":
        b = b + 1
        a[i] = b 

print(a)        
