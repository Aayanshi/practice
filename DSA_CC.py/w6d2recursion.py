'''Week 6- Day 2 : Coding Challenge
(Maximum marks -15)
Q-1 ) Recursive implementation of atoi() function:(5 marks)
Atoi() function converts a string into an integer.
eg:
st = “1234” is a string.
if we perform,
st + 1
this results in error since “st” is a string and 1 is an integer, and,
st + “1”
this will append 1 into 1234. Giving us 12341.
write a function that converts the above variable ‘st’ into an integer (so that we
can perform mathematical operations on it).
Let’s call our function “myAtoiRecursive()”, it should,
myAtoiRecursive(st) + 1
should give us 1235 (that is 1234+1).
As shown in image below:
Sample input:  
“1234”
Sample output:
1234'''

# iterative way
s = input("Enter number= ") # taking input = 2672

n = len(s)   # calculating length of the input

c1 = 0  # declaring an empty container to store something

c2 = 1  # another container to perform some operations

for i in range(n-1,-1,-1): #using length as range form backwards s[i] = 2, 6,7,2

    c1 = c1 + int(s[i]) * c2  # 0+ (2x1) = 2, 2+7x10 = 72, 72+6*100= 672, 672+2*1000= 2672

    c2 = c2 * 10 # c2 = 1x10 = 10, c2 = 10x10= 100, c2 = 100x10= 1000, 

print(c1+ 1)   

# recursive'''





'''def huh(sting):
    
    n = len(sting)
    count1 = 0
    count2 = 1
#   count1 = count2 * huh(int(n-1))
#  count2 = count2 * 10

    return count2

ci = huh(sting)
print(ci)
'''

sting = input("Enter Number= ")
def myAtoiRecursive(sting, c):
    length = len(sting)
    if length == 1:
        return int(sting)+(c*10)

    c = int(sting[0])+(c*10)
    return myAtoiRecursive(sting[1:], c)





b = myAtoiRecursive(sting,0)
print(b+1)


    
    
    
    




'''You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order.
 If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

Example 1:

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.
Example 2:

Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.
Example 3:

Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i], target <= 100'''

'''arr = [1,2,5,2,3,1,2,2,3,5,7,7,7,7,9,13,8,3,2,7,17,28]
nums = sorted(arr)
target = int(input(f"Choose some number from {nums} or by choice = "))

l = 0 
h = len(nums)-1
s = -1
li = [ ]
while l <= h :
    mid = (l+h)//2
    if nums[mid] < target:
        l = mid + 1
    
    elif nums[mid] > target :
        h = mid - 1

    else:
        s = mid
        h = mid - 1
    
#li.append(s) lower bound

l = 0 
h = len(nums)-1
p = -1 
while l<=h :
    mid = (l+h) // 2
    if nums[mid] < target:
        l = mid + 1
    
    elif nums[mid] > target :
        h = mid - 1

    else:
        p = mid
        l = mid + 1
    
#li.append(p) upper bound
for i in range(s,p+1):
    if s != -1 :
        li.append(i)

        
print(li)
'''






















































































