'''Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.

 

Example 1:

Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
Example 2:

Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.'''

nums = [10,20,30,5,10,50]
p1 = 0
p2 = 1
'''maxi = nums[p1]
runi = nums[p1]
while p2 < nums'''

r = []

'''for i in range(len(nums)):
    c = 0
    if i == len(nums)-1:
        if nums[i] > nums[i-1]:
            c = c + nums[i] 
            r.append(c)
    elif nums[i] < nums[i+1]: 
        c = c + nums[i] 
        r.append(c)    
print(r)    '''
c = nums[0]
r.append(c)
for i in range(1,len(nums)):
    if nums[i]< nums[i-1]:
        c = nums[i]
        r.append(c)

    else:
        c = c+nums[i]
        r.append(c)

    


    
    
print(r)
