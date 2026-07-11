class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        for x in range(n+1):
            i=0
            while i<n and nums[i]<x:
                i+=1
            if n-i==x:
                return x
        return -1
        