class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n=len(senate)
        r=deque()
        d=deque()
        for i,c in enumerate(senate):
            if c=="R":
                r.append(i)
            else:
                d.append(i)
        while r and d:
            a=r.popleft()
            b=d.popleft()
            if a<b:
                r.append(a+n)
            else:
                d.append(b+n)
        return "Radiant" if r else "Dire"