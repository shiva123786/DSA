class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n=len(nums)
        def prime(x):
            fact=set()
            d=2
            while d*d <=x:
                while x%d==0:
                    fact.add(d)
                    x//=d
                d+=1
            if x>1:
                fact.add(x)
            return fact
        fact=[prime(x) for x in nums]
        ans=0
        left=0
        count={}
        for right in range(n):
            for p in fact[right]:
                count[p]=count.get(p,0)+1
            while len(count)>k:
                for p in fact[left]:
                    count[p]=count[p]-1
                    if count[p]==0:
                        del count[p]
                left+=1
            ans=max(ans,right-left+1)
        return ans
                    
                