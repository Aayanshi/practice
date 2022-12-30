def merge(a,b):
    p1 = 0
    p2 = 0
    m = len(a)
    n = len(b)
    c = [ ]
    while p1<m and p2<n:
        if a[p1] < b[p2]:
            c.append(a[p1])
            p1 = p1 + 1
        else:
            c.append(b[p2])
            p2 = p2 + 1    

    while p1<m:
        c.append(a[p1])
        p1 = p1 + 1

    while p2<n:
        c.append(b[p2])
        p2 = p2 + 1

    return c       


if __name__ == "__main__":
    a = [1,3,5,7]
    b = [2,4,6]    
    re = merge(a,b)
    print(re)