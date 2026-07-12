class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans=0
        while any(nums[i]>nums[i+1]for i in range(len(nums)-1)):
            k=0
            s=nums[0]+nums[1]
            for i in range(1,len(nums)-1):
                if nums[i]+nums[i+1]<s:
                    s=nums[i]+nums[i+1]
                    k=i
            nums=nums[:k]+[nums[k]+nums[k+1]]+nums[k+2:]
            ans+=1

        return ans