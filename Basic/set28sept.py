s1 = set([4])
print(s1)
#it retain unique value
s1.add(1)
s1.add(2)
s1 = {1,2,3}
#s2 = s1.union({1,6,3})
s2 = {0,2,8,7,67}
#unordered #unindex not sorted lucky meee
s2.remove(2)
print(s1.union(s2))
print(s1.intersection(s2))
print(s2.isdisjoint(s1))
print(max(s2))
#isdisjoint means having two different sets totally
#set.intersection

#way to write string
set3 = "iamcutebutnotforyou"
print(set(set3))

#way to write dict in set only keys likhega
dict1 = {"aaina" : 3,  "kubs" : 0}
print(set(dict1))



print(type(s1))
s2 = set ([1,2,3,4,5,6])
print(s2)


Aainu = [20,17,62,62,12,2,2,34,2,20,62]
s1 = set(Aainu)
print(list(s1))

