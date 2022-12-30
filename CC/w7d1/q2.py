'''Q-1 ) Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/submissions/
(5 marks)
Given two integer arrays nums1 and nums2, return an array of their
intersection. Each element in the result must be unique and you may return
the result in any order.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
'''

'''def intersection(a,b):
    p1 = 0
    p2 = 0
    m = len(a)
    n = len(b)
    c = []

    while p1<m and p2<n :
        if a[p1] != b[p2]:
            p1 = p1 + 1
        else:
            c.append(b[p2])
            p1 = p1 + 1
            p2 = p2 + 1
        
    return c
                    

a = [1,3,2]
b = [2,4,7,1,3,2]                 
re = intersection(a,b)
print(re)'''


def intersect(a,b):
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j] :
                c.append(a[i])

    return list(set(c))            
    
a = [1,3,2]
b = [2,4,7,1,3,2] 
re = intersect(a,b)
print(re)