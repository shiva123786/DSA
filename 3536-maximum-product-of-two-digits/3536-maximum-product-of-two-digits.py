class Solution:
    def maxProduct(self, n: int) -> int:
        digit=list(map(int,str(n)))
        digit.sort(reverse=True)
        return digit[0]*digit[1]