'''Given a sorted array of distinct integers and a target value, return the index if the target is found.
 If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4'''


nums = [1,3,5,6]
target = int(input("pick number= "))


def index(nums,target):
    l = 0
    h = len(nums)-1
    
    while l<=h:
        
        mid = (l+h)//2
        
        if nums[mid] > target :
            h = mid - 1
        
        elif nums[mid] < target :
            l = mid + 1 

        elif nums[mid] == target:
            return mid
    
        me = mid+1 
    
    return me      


re = index(nums,target)
print(re)        



nums = [1,3,5,6]
target = int(input("pick number= "))


def index(nums,target):
    l = 0
    h = len(nums)-1
    while l<=h:
        mid = (l+h)//2
        
        if nums[mid] == target :
            return mid
        
        elif nums[mid] > target :
            h = mid -1 

        else:
            l = mid +1
            res = l
            
    return res        


re = index(nums,target)
print(re)
                                                                                                                                