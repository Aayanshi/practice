# Creation of Set in Python
 
# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1) 

# Creating a Set with
# the use of a String
set1 = set("AainaisGorgeous")
print("\nSet with the use of String: ")
print(set1)
 
# Creating a Set with
# the use of Constructor
# (Using object to Store String)
String = 'aainaismostbeautiful'
set1 = set(String)
#print("\nSet with the use of an Object: " )
print(set1)
 
# Creating a Set with
# the use of a List
set1 = set(["aaina", "love", "food"])
print("\nSet with the use of List: ")
print(set1)

# Creating a Set with
# a List of Numbers
# (Having duplicate values)
set1 = set([1, 2, 17, 4, 17, 17, 3, 4, 5])
print("\nSet with the use of Numbers: ")
print(set1)
 
# Creating a Set with
# a mixed type of values
# (Having numbers and strings)
set1 = set([1, 17, 'Aaina', 4, 'love', 6, 'Dogs'])
print("\nSet with the use of Mixed Values")
print(set1)

# Creating a Set with
# a dictionary
# (having keys and values)
blonde_dict = {1: "curlyblonde", 2: "redhead", 3: "brunette"}
blonde_set = set(blonde_dict)
print("blonde_dict as a set: ", blonde_set)
# it will take only keys as set items