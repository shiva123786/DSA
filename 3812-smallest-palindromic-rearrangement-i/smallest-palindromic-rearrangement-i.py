class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt=Counter(s)
        left=""
        mid=""
        for ch in sorted(cnt):
            left+=ch*(cnt[ch]//2)
            if cnt[ch]%2:
                mid=ch
        return left+mid+left[::-1]