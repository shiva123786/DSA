
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s2=set(nums1)
        s1=set(nums2)
        return [list(s2-s1), list(s1-s2)]
        
        
