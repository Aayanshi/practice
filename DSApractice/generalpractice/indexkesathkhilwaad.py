
## list me input lagna

'''l = list(map(int,input("here= ").split()))
print(l)'''
'''
a = [0,1,2,3,6,4,5,7]
b = ["life","is","complicted","as","this","code","right","now"]
c = [12,23,34,45,56,67,78,89]


f = 0
for i in a:
    c[i] = b[f]
    f = f+1

print(c)
print(b)   
'''
n = [10,2,1,5,6]
evn1 = [] #index se pehle
odd1 = []

for i in range(len(n)): #index
    if i % 2 == 0:
        evn1.append(i)
    else :
        odd1.append(i)    

print(evn1,odd1)

ement = []
oment = []

for i in n:
    if i % 2 == 0:  # element
        ement.append(i)
    else :
        oment.append(i)    



ement.sort()             # sorted both
oment.sort(reverse= True)

print(ement,oment)

#evn1=[0, 2, 4]                                           #odd1=[1, 3]
#ement=[2, 6, 10]                                         #oment=[5, 1]
#n = [10,2,1,5,6]



t = 0
for i in evn1:
    n[i] = ement[t]
    t = t + 1
print(n)

v = 0
for i in odd1:
    n[i] = oment[v]
    v = v + 1
print(n)
