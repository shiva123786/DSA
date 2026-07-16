class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        sol=[]
        for x in nums:
            for d in str(x):
                sol.append(int(d))
        return sol
            
        