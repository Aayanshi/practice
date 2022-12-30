'''Q - 1 ) Write a code that takes input a string of integers, separated by
space, and return a list of integers:
Sample Input:
“1 2 3 4 5 6 7”
Sample output:
[1,2,3,4,5,6,7]
not [‘1’,’2’,’3’,’4’,’5’,’6’,’7’]'''

#ans.1

aaina = "1 76 2"
inu = "pokxsjxklsnjn899"
print(aaina.split()) #split replacethe spaces with commma '''

n = str(input("enter your number with spaces= "))
p =n.split()
print((p))
c = []
for i in p:
    c.append(int(i))

print(c) 

         

                  
