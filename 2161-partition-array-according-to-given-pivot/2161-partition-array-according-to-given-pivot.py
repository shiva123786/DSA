class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        ans=[0]*n
        l=0
        for x in nums:
            if x<pivot:
                ans[l]=x
                l+=1
        m=l
        for x in nums:
            if x==pivot:
                ans[m]=x
                m+=1
        r=m
        for x in nums:
            if x>pivot:
                ans[r]=x
                r+=1
        return ans