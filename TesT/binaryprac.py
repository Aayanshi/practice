###### binary search ##########

'''(7.5 marks)
Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1'''

'''num = [-1,0,3,5,9,12]
target = int(input("here= "))



def array(num,target):
    l = 0
    h = len(num)-1

    while l <= h :
        mid = (l+h) // 2
        if num[mid] < target :
            l = mid+1
    
        elif num[mid] > target :
            h = mid - 1
    
        else :
            return mid
    return -1                    

ans = array(num,target)
print(ans)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(num)-1
        while l <= h:
            mid = (l+h)//2
            if num[mid] > target:
                h = mid - 1
            elif num[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1    
'''



''' q2
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the
integer part of the result is returned.
Note: You are not allowed to use any built-in exponent function or operator, such
as pow(x, 0.5) or x ** 0.5.
Example 1:
Input: x = 4
Output: 2
Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is
truncated, 2 is returned.
'''
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0 
        h = x
        mid = (l + h)//2
        if  x == 0 or x == 1 :
            return x
        while l < h:
            s = mid * mid 
            if s == x :
                return(mid)
            elif s < x :
                l = mid + 1 
            else:  
                h = mid 
            mid = (l+h)// 2    
        return(mid-1)
'''



'''q2 
Given an array of integers nums sorted in ascending order, find the starting and
ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]'''

n = [5,7,7,8,8,10]
target = int(input("here= "))
l = 0
h = len(n)-1
s = -1

while l<=h:  #lower bound
    mid = (l+h)//2
    if n[mid] < target :
        l = mid + 1

    elif n[mid]> target :
        h = mid - 1

    else :
        s = mid 
        h = mid - 1 

l = 0
h = len(n)-1
p = -1

while l<=h:
    mid = (l+h)//2
    if n[mid] < target :
        l = mid + 1

    elif n[mid]> target :
        h = mid - 1

    else :
        p = mid 
        l = mid + 1

print(s,p)
