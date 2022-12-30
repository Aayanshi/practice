#way to get easy sum within list for two pointers

def runing(a):
    r = []
    r.append(a[0])
    for i in range(1,len(a)):
        r.append(a[i]+ r[i-1])
    return r

def runtime(i,j,r):
    if i == 0:
        return r[j]
    return r[j] - r[i-1]    


a = [1,2,6,-1,4,5,8,11,4,-2,15]
r = runing(a)
print(r)
v = runtime(3,7,r)
print(v)