'''Q-1 ) Select the appropriate code that performs selection sort.
a)
for j in range(n):
min = j
for k in range(j+1,n):
if(arr[k] < arr[min])
min = k
temp = arr[min]
arr[min] = arr[j]
arr[j] = temp
b)
for j in range(n):
min = j
for k in range(j+1,n+1):
if(arr[k] < arr[min])
min = k
temp = arr[min]
arr[min] = arr[j]
arr[j] = temp
c)
for j in range(n):
min = j
for k in range(j+1,n+1):
if(arr[k] > arr[min])
min = k
int temp = arr[min]
arr[min] = arr[j]
arr[j] = temp
d)
for j in range(n):
min = j
for k in range(j+1,n+1):
if(arr[k] > arr[min])
min = k
int temp = arr[min]
arr[min] = arr[j]
arr[j] = temp
'''





'''Q-3 ) Write a program to perform selection sort without using an auxiliary
(extra) list, and tell the time complexity and space complexity of your
code. (5 marks)
'''
'''n = [7,5,3,8,2,9,1]
c = []

for i in range(len(n)):
    mi = n[0]
    me = 0
    for i in range(len(n)):
        if n[i] < mi:
            mi = n[i]
            me = i
    c.append(mi)
    n.remove(mi)    

print(c)

l = len(n)

for i in range(l):
    mini = i
    for j in range(i+1,l):
        if n[i] > n[j]:
            mini = j
            n[i],n[j] = n[j],n[i]
            
print(n)'''



'''li = len(n)
for i in range(len(n)):
    mi = i
    for j in range(i+1,len(n)):
        if n[j] < n[i]:
            mi = j
    (n[i],n[mi])=(n[mi],n[i])

print(n)
'''
aainu = [7,5,3,8,2,9,1]
n = len(aainu)

for i in range(n):
    mini= i
    for j in range(i+1, n):
        if aainu[i]>aainu[j]:
            mini = j
            (aainu[i],aainu[mini])= (aainu[mini], aainu[i])
print(aainu)

