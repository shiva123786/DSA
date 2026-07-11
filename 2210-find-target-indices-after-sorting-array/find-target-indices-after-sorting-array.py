class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        a=sum(x<target for x in nums)
        b=sum(x==target for x in nums)
        return list(range(a,a+b))        