#merge function in merge sorting in one list 

def mergefunc(a,st1,end1,st2,end2):
    p1 = st1
    p2 = st2
    c = []

    #1st loop
    while p1<=end1 and p2<=end2:
        if a[p1] < a[p2]:
            c.append(a[p1])
            p1 = p1 + 1

        else:
            c.append(a[p2])
            p2 = p2 + 1

    # 2nd loop 
    while p1<=end1:
        c.append(a[p1])
        p1 = p1 + 1

    # 3rd loop 
    while p2<=end2:
        c.append(a[p2]) 
        p2 = p2 + 1


    idx = 0 
    while idx < len(a):
        a[idx] = c[idx]
        idx +=1

    return a  


a = [ 1,3,5,7,2,4,6,8]
re = mergefunc(a,0,3,4,7)
print(re)



