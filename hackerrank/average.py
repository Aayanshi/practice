'''The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.'''

d = {"a": [14,15,11], "b": [18,7,33], "c": [1,6,9],"t" : [7,13,12]}
print(d)
mark = []
n = input(f"name through this {d}=  ")
for i in d.keys():
    if i == n :
        mark = d[i]
c = 0
print(mark)  
for i in mark:
    c = i + c
    d = c // len(mark)
print(d)


