class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=set(nums1)
        sol=set()
        for x in nums2:
            if x in s:
                sol.add(x)
        return list(sol)