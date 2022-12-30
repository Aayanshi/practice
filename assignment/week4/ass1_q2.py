
'''Q2. Take input from user items and their quantity. And then print the item
with the maximum quantity.
Eg.
Apple 5
Banana 10
Grapes 50
Output: Grape'''

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