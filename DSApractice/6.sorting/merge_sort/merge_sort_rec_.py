
def merge_function(a,st1,end1,st2,end2):
    p1 = st1
    p2 = st2
    c = []

    while p1<=end1 and p2<=end2 :
        if a[p1] < a[p2]:
            c.append(a[p1]) 
            p1 = p1 + 1
        else:
            c.append(a[p2])
            p2 = p2 + 1

    while p1 <= end1:
        c.append(a[p1]) 
        p1 = p1 + 1

    while p2 <= end2:
        c.append(a[p2])
        p2 = p2 + 1    

    id = 0
    while id <len(c):
        a[st1+id] = c[id]
        id = id + 1 

    return a       


def merge_sort(a,low,high):
    mid = (low+high) // 2
    if low == high :
        return
    merge_sort(a,low,mid)
    merge_sort(a,mid+1,high)
    merge_function(a,low,mid,mid+1,high)


aaina =[2,4,1,6,3,7,7,0,12,-1,5]
merge_sort(aaina,0,len(aaina)-1)     
print(aaina)   