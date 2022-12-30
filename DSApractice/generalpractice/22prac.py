# sorting

#selection method
ar = [8,5,6,3,9,1]
li = [ ]

for i in range(len(ar)):
    mi = ar[0]
    me = 0
    for i in range(len(ar)):
        mi > ar[i]
        me = i
    li.append(mi)
    ar.remove(mi)

print(li)




# buble
l = len(ar)
for i in range(0,l):
    minu = i
    for j in range(i+1,l):
        if ar[i] > ar[j]:
            minu = j
            (ar[i],ar[j]) == (ar[j],ar[i])

print(ar)


# rat maize
