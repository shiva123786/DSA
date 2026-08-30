class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        first={}
        last={}
        for i,x in enumerate (nums):
            if x not in first:
                first[x]=i
            last[x]=i
        return sum(last[x]-first[x]+1==nums.count(x) for x in first)