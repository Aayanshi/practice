# convert input into list

'''n = input("here= ")
b = list(map(int,n.split()))
print(b)'''
'''d = [1, 44, 23, 28, 62, 5]
#    0,  1,  2,  3,  4, 5
bl = [23, 28, 5, 44, 62, 1]

evenindex = []
oddindex = []

for i in range(len(d)):
    if d[i]%2== 0:
        evenindex.append(i)
    else:
        oddindex.append(i)
print(evenindex)
print(oddindex)

evenelement = []
oddelement = []


for i in d:
    if i%2 == 0:
        evenelement.append(i)
    else:
        oddelement.append(i)

print(evenelement)
print(oddelement)

evenlist = sorted(evenelement)
oddlist= sorted(oddelement, reverse= True)
print(evenlist)
print(oddlist)

e= 0
for i in evenindex:
    d[i] = evenlist[e]
    e = e+1
enu = 0
for i in oddindex:
    d[i]= oddlist[enu]
    enu = enu+1

print(d)'''



a = ["blue", "black", "red", "purple", "pink", "yellow", "white"]
b  = [23, 25, 20, 34, 45, 56,67,78,98,100,87,62,54,45]
c = [0,1,1,3,1,2,4,2,1,2,0] 
le = len(c) 

r = 0
for i in c:  
    b[i]=a[r]
    r = r+1
    print(b)