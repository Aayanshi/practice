'''You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1'''




def mergao(n1,n2):
    p1 = 0
    p2 = 0
    m = len(n1)
    n = len(n2)
    c = []
    while p1<m and p2<n :
        if n1[p1] < n2[p2] :
            c.append(n1[p1])
            p1 = p1 + 1

        else :
            c.append(n2[p2])
            p2 = p2 + 1

    while p1<m :
        c.append(n1[p1])
        p1 = p1 + 1

    while p2<n :
        c.append(n2[p2])
        p2 = p2 + 1

    return c    

'''    idx = 0
    while idx < len(c) :
        n1[idx] = c[idx]
        idx = idx + 1'''




if __name__ == "__main__" :
    n1 = [0,0,1,2,3,]
    n2 = [0,2,5,6]
    re = mergao(n1,n2)
    print(re)

