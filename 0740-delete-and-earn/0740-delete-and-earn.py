class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        m=max(nums)
        a=[0]*(m+1)
        for x in nums:
            a[x]+=x
        p=c=0
        for x in a:
            p,c=c,max(c,p+x)
        return c
