class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        c = 0
        for i in range(m):
            if nums1[i] == 0 :
                nums1[i] == nums2[c]
                c = c + 1
    
        st1 = 0
        ed2 = m-1
        ed1 = (st1+ed2)//2
        st2 = ed1+1
        def merge(nums1,st1,ed1,st2,ed2):
            p1 = st1
            p2 = st2
            f = []
            while p1<=ed1 and p2<=ed2:
                if nums1[p1]<nums1[p2]:
                    f.append(nums1[p1])
                    p1 = p1 + 1
                else :
                    f.append(nums1[p2])
                    p2 = p2 + 1

            while p1<=ed1:
                f.append(nums1[p1])
                p1 = p1 + 1

            while p2<=ed2:
                f.append(nums1[p2])
                p2 = p2 + 1

            idx = 0
            while idx < len(f):
                nums1[idx] = f[idx] 
                idx = idx + 1
        return nums1 