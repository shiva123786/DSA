class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        mp={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans=['']
        for d in digits:
            ans=[x+c for x in ans for c in mp[d]]
        return ans