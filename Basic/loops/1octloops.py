#first loop 1. for item in ____
list1 = [["aaina",1] ,["kubs",2] 
        ,["all",15],["baby",4]]

for item, choclates in list1 :
    print(item, "will eat choclate" , choclates)

list1 = [["aaina",1] ,["kubs",2] 
        ,["all",15],["baby",4]]
dict1 = dict(list1)  
print(dict1)  

for item in dict1:
    print(item)

for item, choclates in dict1.items() :
    print(item, "will eat choclate" , choclates)

#quiz
list2 = [1,4,"me", 78, 20, 5, 77, "you",33.5]
for item in list2:
    if type(item) == (int) and item>6 :
        print(item)
    elif type(item) == (float) and item>6:
        print(item)
               
dict2 = {"aaina":"me", "kubs":"penguin","us":"happy"}
for item, key in dict2:
    print(key, "my")





list1 = ["hey",1, "o",6,34,34.6]
for item in list1:
    print("ohk", item)