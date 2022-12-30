'''q1. Write a Python program to count the number of characters (character frequency) in a string. 
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}'''





'''v = "google.com"
k = len(v)
di = { }
for i in v:
    l = di.keys()
    if i in l :
        di[i] = di[i] + 1
    else:
        di[i] = 1

print(l)    
print(di) '''
'''    for i in v:
    fucku = di.keys()
    if i in fucku:
        di[i] = di[i] + 1
    else:
        di[i] = 1    
     '''

'''q2. Write a Python program to remove the characters which have odd index values of a given string.
sample input: "abcde"
output: "bd"  '''

'''n = input("here= ")
for i in range(len(n)):
    if i % 2 == 0:
        print(n[i],end="")
    else:
        continue


print( )'''  
'''q3. Write a Python program that accepts a comma separated sequence of words as input and prints the unique 
words in sorted form (alphanumerically). 
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,
hint: use array to store and operate
'''
'''l = [ ]
for i in range(5):
    n = input("enter= ")
    l.append(n)
x = sorted(l)    
for you in x:
    print(you,end=",")'''



'''q4. Write a Python program to count and display the vowels of a given text'''
n = input("enter= ")
v = ""
for i in n:
    if i in "aeiouAEIOU":
        v = v + i

print(v)        
