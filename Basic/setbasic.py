#sets in python
#unordered, unindexed, mutable 
# functions for sets : 
# len()  for length of set
# max()    for maximum value in set
# min()   for minimum value in set
# sum()   for sum of all elements
# any(), all(), sorted()

# set is created with curly braces
set1 = {1, 2, 3,"weirdo", 88, 45}
print(set1)
print(type(set1))

# a set is mutable but can not contain mutable items
'''set2 = {23, 25, 29, 47.7, "paridha", [12, 2, 17, 62]}
print(set2)'''
#will throw an error as list inside the set is a mutable item list ke sath integer, string, float bhi hai

#another way to declare a set (empty set too)
#example 
set3 = set()        #we just declared an empty set
#but if we do it this way 
set4 = {} 
print(type(set4)) #it will show its type as dict 
                  #as its the syntax for creating an empty dict

#set properties
set5 =  set([1,2,4,7,99.17])  #will take only one iterable item
print(set5)
'''set6 = set(123,[11, 23, "brew"]) #will throw error as more than one arguments
print(set6)'''

#sort function(almost same as list)
woodoo = sorted(set5)
print(woodoo)

#discard function and remove function(used to delete an item from set)
'''both will delete the item from set but if the targeted item is not 
present in set remove function will throw error while discard function will 
do it without any error'''

setfool = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])
 
# Removing elements from Set
# using Remove() method
setfool.remove(5)
setfool.remove(8)
print("\nSet after Removal of two elements: ")
print(setfool)
 
# Removing elements from Set
# using Discard() method
setfool.discard(8)
setfool.discard(8)
print("\nSet after Discarding two elements: ")
print(setfool)

#pop method 
setfool.pop()
print("\nSet after popping an element: ")
print(setfool)


# Addition of elements in a Set
 
hotset = set()
print("Initial blank Set: ")
print(hotset)
 
# Adding element and tuple to the Set
set1.add(8)
set1.add(9)
set1.add((6, 7)) 
#(6,7) is tuple
print("\nSet after Addition of Three elements: ")
print(hotset)

# Addition of elements to the Set
# using Update function
coolset = set([4, 5, (6, 7)])
coolset.update([10, 11])
print("\nSet after Addition of elements using Update: ")
coolset.clear()
print(coolset)

#for clearing all elemets frrom set
#setname.clear()