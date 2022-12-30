def runnin(a):
    r = []
    r.append(a[0])
    for i in range(1,len(a)):
        r.append(a[i]+r[i-1])
    return r


def runtime(i,j,r):
    if i == 0 :
        return r[j]
    
    return r[j]-r[i-1]
        

       
        

if __name__ == "__main__":
    a = [2,4,-2,6,13,11,1,5,7]
        #0 1  2 3  4  5 6 7 8 

    res = runnin(a)
    print(res)    
    re = runtime(2,5,res)  
    print(re)
    
    






