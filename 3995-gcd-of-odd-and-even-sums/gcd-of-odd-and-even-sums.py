class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumodd=n*n
        sumeven=n*(n+1)
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        return gcd(sumodd,sumeven)