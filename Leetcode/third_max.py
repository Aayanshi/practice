
'''Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
'''
nums = [7,9,6,4,3,2,9,6]
c = list(set(nums))
v = sorted(c,reverse=True)

if len(c)< 3 :
    print(v[0])
else :
    print(v[2])
