class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d={}
        for x in nums:
            d[x]=d.get(x,0)+1
        return sum(x for x,v in d.items()if v==1)