
'''Q - 2 ) Find largest number in a list, and second largest number, (without
using inbuilt functions).
eg:
A = [1,3,4,5,8,1,2,3,4,9,6,9]
return 9 and 8.
Write time and space complexity of your code.'''

a = [1,3,4,5,8,1,2,3,4,9,6,9]
mx = 0
mx2 = 0
for i in a: 
    if mx < i:
        mx = i 

for i in a :           
    if mx2 <i and mx > i:
        mx2 = i

print(mx , mx2)    