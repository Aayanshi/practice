a = [1,2,3,4,5,6]
    #0 1 2 3 4 5 
b = len(a)
l = 0
h = b
c = []
mid = (l+h)//2 

#median
if b % 2 == 0 :
    midean = (a[mid-1] + a[mid]) / 2
    c.append(midean)
else :
    midean = a[mid]
    c.append(midean)

#mean
cd = 0 
for i in range(b-1):
    cd = cd + i
mean = cd / len(a) 


print(c)           
'''print(midean,mid,b) 
print(mean,cd)  '''



