class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=float("inf")
        for x in nums:
            s=0
            while x:
                s+=x%10
                x//=10
            ans=min(ans,s)
        return ans
        