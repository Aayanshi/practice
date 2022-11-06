#dictionary is key value pairs
'''d1 = { }
print(type(d1))'''


'''dic2 = {"aaina" : "code" ,"mummy" : "khana" , "papa" : "store" ,
        "arna" :{"m" : "college", "e": "ghumna", "n": "sona"}}'''



#5keys / items
'''print(dic2.keys())
print(dic2.items())'''



#4other func. of dic
'''print(dic2.get("mummy"))
dic2.update({"me" : "write"})'''



#3copy n del into new dic
'''d3 = dic2.copy()           
                                
del d3["arna"]
print(d3)'''


#2add into dic
'''dic2["coco"] = "biscuit"
dic2["main"] = "design"
dic2["mummy"] = "job"
del dic2["aaina"]
print(dic2)'''

#1dic me bhi dic define karna
'''print(type(dic2))
print(dic2["aaina"])
print(dic2["papa"])
print(dic2["arna"] ["n"])'''


#practice



'''myd1={"1": "wakeup",
     "2" : "yoga", 
     "3" : "code" , 
     "4" :"design" ,
      "5": "sleep" , "food" : {"m": "breakfast","n" : "lunch", "e" :"dinner" }}
print(myd1["2"])
print(myd1["4"])
print(myd1["food"] ["n"])
myd1.update({"6" : "sleep"})
del myd1["4"]
d2 = myd1.copy()
del d2["5"]
print(d2)
print(myd1.keys())
print(myd1.items())

#wooooooooooooooh i did 
here award goes to u


d2 = myd1.copy()
del d2(["5"]) 
print(d2)

aaina = dict({"me" : "sleep" , "huh" : "ohk" , })
print(type(aaina))
print(aaina)
print(aaina ["me"])'''


#practice with kub changing list into dict
#two ways

''' way 1
mylist = dict([("khana","pina"), ("sona" ,"padhna"), ("design","code") ])
print(type(mylist)
'''

mylist = [("khana","pina"), ("sona" ,"padhna"), ("design","code") ]
d1 = dict(mylist)
print(d1)
