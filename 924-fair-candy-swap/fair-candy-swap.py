class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        d=(sum(aliceSizes)-sum(bobSizes))//2
        s=set(bobSizes)
        for x in aliceSizes:
            if x-d in s:
                return [x,x-d]