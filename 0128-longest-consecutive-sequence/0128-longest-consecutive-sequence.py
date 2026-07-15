class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        ans=0
        for x in s:
            if x-1 not in s:
                cur=x
                cnt=1
                while cur+1 in s:
                    cur+=1
                    cnt+=1
                ans=max(ans,cnt)
        return ans
        