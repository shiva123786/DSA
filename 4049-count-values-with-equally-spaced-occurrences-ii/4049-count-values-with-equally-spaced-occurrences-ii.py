class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        d={}
        for i,x in enumerate(nums):
            d.setdefault(x,[]).append(i)
        ans=0
        for p in d.values():
            if len(p)>=3:
                diff=p[1]-p[0]
                if all(p[i]-p[i-1]==diff for i in range(2,len(p))):
                    ans+=1
        return ans