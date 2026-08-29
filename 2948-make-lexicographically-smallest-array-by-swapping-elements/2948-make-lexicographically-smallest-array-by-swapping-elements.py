class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr=sorted((x,i) for i,x in enumerate(nums))
        ans=nums[:]
        i=0
        while i<len(nums):
            j=i
            while j+1<len(nums) and arr[j+1][0]-arr[j][0]<=limit:
                j+=1
            indices=sorted(x[1] for x in arr[i:j+1])
            values=sorted(x[0] for x in arr[i:j+1])
            for k in range(len(indices)):
                ans[indices[k]]=values[k]
            i=j+1
        return ans