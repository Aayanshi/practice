n = 5
x = 1
y = 2
z = 3
ls = []  

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n and i+j+k < n :
                sum = [i,j,k]
                ls.append(sum)

print(ls)    

print( )
'''lets find runner up (higgest se second)'''
l = [2,7,4,11,13,2,6,4,17,17,13,18]
l.sort()
print(l)
c = set(l)
print(c)
print(list(c))
d = list(c)
print(d[-2])


