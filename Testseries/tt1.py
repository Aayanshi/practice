'''The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.'''

d = {"a": [14,25,9] ,"b": [15,22,6], "d": [11,20,10] ,"e": [13,23,6], "f" :[16,24,8]}
n = input(f"choose name from {d.keys()} for average marks= ")
mark = []
for i in d.keys():
    if i == n:
        mark = d[i]
print(f"So, u selected this {n} his marks are {mark}")    

c = 0
for i in mark:
    c = i + c
    d = c // 3

print(f"so the average is {c}")    

#Minion Game
n = input("enter any string= ")
s = 0
k = 0
'''
for i in n:
    if i in n      '''   
