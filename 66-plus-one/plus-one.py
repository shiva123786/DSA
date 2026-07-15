class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=int(''.join(map(str,digits)))
        num+=1

        ans=[int(x) for x in str(num)]

        return ans
        