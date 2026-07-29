class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        self.ans=""
        n=len(s)
        cnt=Counter(s)
        self.ar=[0]*26
        mid=""
        for ch,val in cnt.items():
            if val%2:
                mid=ch
            self.ar[ord(ch)-97]=val//2
        m=n//2
        fact=[1]*(m+1)
        for i in range(1,m+1):
            fact[i]=fact[i-1]*i
        total=fact[m]
        for x in self.ar:
            total//=fact[x]
        if k>total:
            return ""
        def helper(k,ln,pos):
            if ln==0:
                return
            prev=0
            for i in range(26):
                if self.ar[i]==0:
                    continue
                ways=(pos*self.ar[i])//ln
                if prev<k<=prev+ways:
                    self.ans+=chr(i+97)
                    self.ar[i]-=1
                    helper(k-prev,ln-1,ways)
                    return
                prev+=ways
        helper(k,m,total)
        if mid:
            return self.ans+mid+self.ans[::-1]
        return self.ans+self.ans[::-1]