class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c=Counter(nums1)
        sol=[]
        for x in nums2:
            if c[x]>0:
                sol.append(x)
                c[x]-=1

        return sol