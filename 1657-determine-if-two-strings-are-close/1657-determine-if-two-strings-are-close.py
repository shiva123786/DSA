class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a=Counter(word1)
        b=Counter(word2)
        return set(a)==set(b) and sorted(a.values())==sorted(b.values())