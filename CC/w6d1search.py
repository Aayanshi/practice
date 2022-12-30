'''Given an array of integers nums sorted in ascending order, find the starting and
ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]'''

num = [5,7,7,7,8,8,10,30,56,59,66]
l = 0
h = len(num)-1
s = -1
target = int(input("Enter your number= "))
while l<=h :
    mid = (l+h) // 2 
    if num[mid] < target :
        l = mid + 1
    
    elif num[mid] > target :
        h = mid - 1

    else : 
        s = mid
        h = mid - 1

l = 0
h = len(num) - 1
p = -1
while l<=h :
    mid = (l+h) // 2
    if num[mid] < target :
        l = mid + 1

    elif num[mid] > target:
        h = mid - 1      

    else :
        p = mid 
        l = mid + 1    



print(f"[{s},{p}]")  

 
#joint account
def searchRange(nums, target):
    n = len(nums)

    h = n-1
    res = []
    aainu = -1
    while l<=h:
        mid = (l+h)//2
        
        if nums[mid] > target:
            h = mid-1
        elif nums[mid]< target:
            l = mid+1
        else:
            aainu = mid
            h = mid-1
        
    
    
    l = 0 
    h = n-1
    kubs = -1
    while l <= h:
        mid = (l+h)//2
        if nums[mid] > target:
                h = mid-1
        elif nums[mid]< target:
                l = mid+1
        else:
                kubs = mid
                l = mid+1

        res.append(aainu)    
        res.append(kubs)
        return res


print(("kabir is just my friend and i hate him\n")*10, end = "")



