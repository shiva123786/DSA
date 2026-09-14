class Solution:
    def minOperations(self, nums: list[int]) -> int:
        
        maxi=len(str(max(nums)))+1
        even,odd=[],[]

        for l in range(1,maxi+1):
            half=(l+1)//2
            start=10**(half-1)
            end=10**half
            for num in range(start,end):
                s=str(num)
                if l%2:
                    pali=int(s+s[-2::-1])
                else:
                    pali=int(s+s[::-1])
                if pali%2==0:
                    even.append(pali)
                else:
                    odd.append(pali)

        even.sort()
        odd.sort()

        def get_mini(num,lst):
            pos=bisect_left(lst,num)
            ans=float('inf')
            if pos<len(lst):
                ans=min(ans,(lst[pos]-num)//2)
            if pos>0:
                ans=min(ans,(num-lst[pos-1])//2)
            return ans

        total=0
        for num in nums:
            total+=get_mini(num,even if num%2==0 else odd)
        return total