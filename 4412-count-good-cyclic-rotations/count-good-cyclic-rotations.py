class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n=len(nums)
        h=n//2
        total=sum(nums)
        first_sum=sum(nums[0:h])
        second_sum=total-first_sum
        count=1 if first_sum>second_sum else 0
        for shift in range(1,n):
            leaving=nums[shift-1]
            joining=nums[(shift+h-1)%n]
            first_sum=first_sum-leaving+joining
            second_sum=total-first_sum

            if first_sum>second_sum:
                count+=1
        return count