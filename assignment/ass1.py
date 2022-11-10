# oops ,list ,dict 
'''Q1. Count no occurrences of a word in a string, where the word is given by
a user.
s = “hello a hello hi hello ok hello”
word: = hello
output: 4'''


'''Q2. Take input from user items and their quantity. And then print the item
with the maximum quantity.
Eg.
Apple 5
Banana 10
Grapes 50
Output: Grape'''

'''Q-3) Create a class Speed and add a method to convert speed from
kilometers per hour to meter per sec ans. is in speed.py'''

#ans1.
b = 0 
n = input("enter here=  ")
m = n.split()
t = input("enter the word u wannt to count= ")
for i in m:
    if t == i:
        b = b + 1

    else:
        continue

print(b)    


'''apple:3, lichi:7, orange:8, peach:5, berries:2'''
    
#ans2.
d = { }
for i in range(1,5):
    t = input("Name of item =  ") #key names
    q = int(input("No.of Quantity in item= ")) #values
    d[t] = q     
max = 0
item = ""
for i in d.keys():
    if max < d[i] :
        max = d[i]
        item = i
        
    else:
        continue
    
print(item) #will print that item(key as i)
             #bhut hard


          
         





 
