class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x=0
        for c in s+t:
            x^=ord(c)
        return chr(x)
        