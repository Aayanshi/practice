#sorting 
# sort()= will sort original one
# sorted()= will create one more sorted list rather changing original one

# sorting = 1.selection sort method 
    #0 1 2 3 4 5
a = [8,5,6,3,9,1]
c = []

for i in range(len(a)):
    mini = a[0]
    minient = 0
    for i in range(len(a)): #step 1
        if mini > a[i] :
            mini = a[i]
            minient = i

    c.append(mini)    
    a.remove(mini)

print(c)        


