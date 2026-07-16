class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=len(nums)
        nums.sort()
        return nums==list(range(1,n))+[n-1]