#strring slicing
a = "aaina"
print(a[0:5:2])
print(a[::-1])

a = [ ]
a.append("aaina")
a.append(17)
a.append(62)
a.insert(2,"birthday")
a.pop(0)
a.pop(1)
'''a.remove(17)'''
#a.delete([2])


bc = [5,77,22,10,34,1,34,78,1000,56]
a.extend(bc)
a.sort()
a.reverse()
b=a.count(34)
bc.clear()
ac = [2,3,4,5,6]
bc.copy()
print(bc)


upset = set([5,77,22,10,34,1,34,78,1000,56])
print(sorted(upset))

b= 4 ** 3
print(b)

stu = {"eng":99 , "hindi": 5 ,
        "maths": 100, "sci": 3}
stu.update({"hindi":95}) 
stu.pop("sci")
stu["draw"] = 55
print(stu)        