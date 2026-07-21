class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pos=defaultdict(list)
        for i,ch in enumerate(s):
            pos[ch].append(i)
        ans=0
        for word in words:
            prev=-1
            ok=True
            for ch in word:
                i=bisect_right(pos[ch],prev)
                if i==len(pos[ch]):
                    ok=False
                    break
                prev=pos[ch][i]
            if ok:
                ans+=1
        return ans