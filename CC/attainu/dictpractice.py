# dictionary practice attainu 
d1= { "k1": 23 ,
          "k2": "file",
          "k3" :[2,4,3,5,5,],
          "k4": (3,5,4,6),
          "k5" : ""  ,
}


for i in d1:
    print(i, "smjh" ,d1[i])

d1.pop("k1")
d1["k1"]=[34]
d3 = d1
print(d1)

print(d3)

print(d1["k3"])
print(d1["k4"][1:3])
print(d1["k2"][1:4:2])
print(d1["k5"])
try :
    d1["k4"].append(3)
except Exception as e:
    print(e)
    

print(d1)


d2 = { "mybday": "paris",
       "winters" : "newyork",
       "diwali" : "ayodhya",
       "holi"   : "barsana",
       "hisbday" : "greece",
       "ftrip" : "rishikhesh",
       "ptrip" : "kedarnath",
       "vacation": "maldvies",
       "mtrip" :{ "banaras" : "bali"},
       "fall" : "darjeeling"}

for k in d2.keys():
    print("kabir please take me to", d2[k],"for", k
)
k ,"take me here with you", d2[k]

"i know you will just reminding you by this dict and now i m going booieee plz take care and take some reastttttttt boo love"


print(list[d2.keys()])
print(list[d2.values()])
print(d1["k4"])


#occurance
l = [1,2,1,1,1,2,3,4,5,5,5]
d = dict()
for i in l:
    if i not in d :
        d[i] = 1
    else:
         i == 1 
         d[i] += 1

print(d)
# max
l = [14,6,2,7,1,10]
max = l[0]
for i in l:
    if max > i :
        continue
    else:
        max = i
    
print(max, "is max")    


'''a:2,b:6,c:19'''

d = { }
for i in range(1,4):
    t = input("Name of item =  ") #key names
    q = int(input("No.of Quantity in item= ")) #values
    d[t] = q     
min = float('inf') #infinity
item = ""
for i in d.keys():
    if min > d[i] :
        min = d[i]
        item = i
        
    else:
        continue
    
print(item,"of quantity",min)     

