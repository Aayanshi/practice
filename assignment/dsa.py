''' Write a code that takes input a string of integers, separated by
space, and return a list of integers:
Sample Input:
“1 2 3 4 5 6 7”
Sample output:
[1,2,3,4,5,6,7]
not [‘1’,’2’,’3’,’4’,’5’,’6’,’7’]
'''
'''b = str(input("enter number= "))
c = list(map(int,b.split()))
print(c)
'''
'''n = str(input("enter your numbers by gap= "))
d = n.split()
print(d)
c = []
for i in d:
    c.append(int(i))

print(c)    
#O = O() and S =S(1)'''


''') Find largest number in a list, and second largest number, (without
using inbuilt functions).
eg:
A = [1,3,4,5,8,1,2,3,4,9,6,9]
return 9 and 8.
Write time and space complexity of your code'''

'''a = [1,3,4,5,8,1,2,3,4,9,6,9]
mx = 0
mi = 0 
for i in a:
    if mx < i:
        mx = i

for i in a :
    if mi < i and mx > i:
        mi = i    
            
print(f"{mx} and {mi} are two maximum numbers respectively")'''
            
''''Given an array arr of integers, check if there exists two integers N and M such
that N is the double of M ( i.e. N = 2 * M).
More formally check if there exists two indices i and j such that :
● i != j
● 0 <= i, j < arr.length
● arr[i] == 2 * arr[j]
Example :
Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5'''

'''l = [2,3,7,8,14,4,16]
n = len(l)

for i in range(n):
    m = i
    if i == 2 * m and n != m:
        print("true")
        
    else :
        print("false")'''
        



'''Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays
and you may return the result in any order.
Example:
Input: nums1 = [1,2,2,1], nums2 = [2,2]'''   
nums1 = [1,2,2,1]
nums2 = [2,2]
l = []
for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i] == nums2[j]:
            l.append((nums1[i]))
            break
            
            

print(l)            