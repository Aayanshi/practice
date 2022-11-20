'''Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Sam"
'''
s = []
l = ["ayan","bakshi","champak","druv","eliana","fakul"]
for i in l:
    p = "Hello ! ," + i
    s.append(p)
print(s)


'''Write a for loop that iterates through a string and prints every letter.
'''
n = input("any word= ")
for i in n:
    print(i,",",end=" ")


print()

'''Write a program which will append each number from the list bebu to the new list cutu if it's positive.
take bebu list input from user
'''
bebu = []
for i in range(1,6):
    b = int(input("number= "))
    bebu.append(b)
print(bebu)
cutu = []
for i in bebu:
    if i >= 0 :
        cutu.append(i)

    else:
        continue

print(cutu)   

'''inu = [2,7,8,9,12,34,56,76,21,5,46]
write a program to print the list consisting sqaure of the elements of list inu in the same sequence.
'''
c = []
inu = [2,7,8,9,12,34,56,76,21,5,46]
for i in inu:
    y = i **2 
    c.append(y)

print(c)    
