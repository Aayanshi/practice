#list cc 


# print elements which are on even index
k = [1,12,60,7,8,9,10,11]
for i in range(len(k)):
    if i % 2 == 0 :
        print( k[i], end=" ")

print()
# print elements which are even number on list
k = [1,24,6,7,8,9,10,11]
for i in k:
    if i % 2 == 0 :
        print(i, end=" ")



print( )

a = [1,2,3,4]
print(a[:len(a):-1])

e = 1
a = [1,3,4,2,8,9,7,0,2,1]
for i in range(len(a)):
    if  a[i] == 2 and e == 1 :
        e = 2
        continue
    
    elif a[i] == 2 and e == 2 :
       print(i, "index 2")

# user se list 
# list comperihennsion
b = input("write what u want into list = ")
c = int(input("how many times do u want this= "))
A = [b for i in range(c)]
print(A)

v = [[0,0,0,] for i in range(3)]
print(v)


#maaping (for)
a = ("4","2","6", "8")
b = list(map(int,a))
print(b)

dt = [ type(i)for i in b]
print(dt)

#add one into list by making func. using map
r =[1,5,3,2]
def add(x):
    return(x + 1)

s = list(map(add,r))
print(s)    

l2 = [ str[::-1] for str in ("amar", "akbar", "ant")]
print(l2)