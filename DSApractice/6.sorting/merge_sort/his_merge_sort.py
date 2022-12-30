
def mergef(inu,st1,ed1,st2,ed2):
    p1 = st1
    p2 = st2
    c = []

    while p1<=ed1 and p2<=ed2:
        if inu[p1] < inu[p2]:
            c.append(inu[p1])
            p1 = p1 + 1
        else:
            c.append(inu[p2])
            p2 = p2 + 1
    
    while p1<=ed1:
        c.append(inu[p1])
        p1 = p1 + 1
        
    while p2<=ed2:
        c.append(inu[p2])
        p2 = p2 + 1


    idx = 0
    while idx < len(c):
        inu[idx] = c[idx]
        idx = idx + 1
    
    return inu



if __name__ == "__main__":
    inu = [1,3,5,7,2,4,6,8]
        #  0 1 2 3 4 5 6 7 
    
    bebu = mergef(inu,0,3,4,7)
    print(bebu)
