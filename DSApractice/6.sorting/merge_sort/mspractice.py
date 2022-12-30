



def merges(a,s1,e1,s2,e2):
    p1 = s1
    p2 = s2
    c = []

    while p1<=e1 and p2<=e2:
        if a[p1] < a[p2]:
            c.append(a[p1])
            p1 = p1 + 1

        else :
            c.append(a[p2])
            p2 = p2 + 1

    while p1 <= e1 :
        c.append(a[p1])
        p1 = p1 + 1

    while p2 <= e2 :
        c.append(a[p2])
        p2 = p2 + 1

    indx = 0
    while indx < len(c)  :
        a[indx] = c[indx]
        indx = indx + 1

    return a


def mergefunc(a,low,high):
    mid = (low+high)//2
    if low == high :
        return
    mergefunc(a,low,mid)
    mergefunc(a,mid+1,high)
    merges(a,low,mid,mid+1,high)    

a = [2,4,6,8,1,3,5,7,9]
    #0 1 2 3 4 5 6 7 8
mergefunc(a,0,len(a)-1)
print(a)