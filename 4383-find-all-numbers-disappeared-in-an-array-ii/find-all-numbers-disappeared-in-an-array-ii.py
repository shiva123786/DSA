class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        s=set(nums)
        ans=[]
        i=lower
        while i<=upper:
            if i not in s:
                start=i
                while i<=upper and i not in s:
                    i+=1
                ans.append([start,i-1])
            else:
                i+=1
        return ans
            
        