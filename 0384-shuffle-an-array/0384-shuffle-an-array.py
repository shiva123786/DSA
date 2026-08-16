class Solution:

    def __init__(self, nums: List[int]):
        self.nums=nums[:]

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        a=self.nums[:]
        for i in range(len(a)-1,0,-1):
            j=random.randint(0,i)
            a[i],a[j]=a[j],a[i]
        return a

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()