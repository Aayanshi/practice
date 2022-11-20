'''Given the names and grades for each student in a class of  students,
 store them in a nested list and print the name(s) of any student(s) having the second lowest grade'''
'''
d = { }
for i in range(4):
    n = input("Student Name= ")
    m = int(input("Student Marks= "))
    d[n] = m 
print(d) 
m = 0
for i in d.keys:
    if '''



'''d = {}
key = []
value = []

for i in range(5):
    n = input("student name = ")
    m = int(input(f"marks of chalu {n}= "))
    d[n] = m
    key.append(n) #name
    value.append(m) #marks
svalue = sorted(set(list(value)))
output = svalue[1]
result= []
for i in d.keys():
    if d[i] == output:
        result.append(i)

for i in sorted(result): #for sorted names
    print(i)'''





d = { }
names = [ ]
marks = [ ]

for i in range(5):
    n = input("your name= ")
    m = int(input("your marks= "))
    d[n] = m 
    names.append(n)
    marks.append(m)

result = [ ]
value = sorted(set(list(marks)))
ans = value[2]
for i in d.keys():
    if d[i] == ans:
        result.append(i)

for i in sorted(result):
    print(i)        







