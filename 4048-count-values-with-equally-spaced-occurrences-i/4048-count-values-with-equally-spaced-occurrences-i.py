class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        pos={}
        for i,x in enumerate(nums):
            if x not in pos:
                pos[x]=[]
            pos[x].append(i)
        ans=0
        for p in pos.values():
            if len(p)==3 and p[1]-p[0]==p[2]-p[1]:
                ans+=1
        return ans