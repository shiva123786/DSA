class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target=sum(nums)-x
        if target<0:
            return -1
        if target==0:
            return len(nums)
        left=curr=max_len=0
        for right in range(len(nums)):
            curr+=nums[right]
            while curr>target:
                curr-=nums[left]
                left+=1
            if curr==target:
                max_len=max(max_len,right-left+1)
        return -1 if max_len==0 else len(nums)-max_len