class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f=0
        s=0
        for num in nums:
            if num>f:
                s=f
                f=num
            elif num>s:
                s=num
        return (f-1)*(s-1)
