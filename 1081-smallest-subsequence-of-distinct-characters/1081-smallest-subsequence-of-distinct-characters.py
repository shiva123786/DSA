class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last={}
        for i,ch in enumerate(s):
            last[ch]=i
        st=[]
        vis=set()
        for i,ch in enumerate(s):
            if ch in vis:
                continue
            while st and st[-1]>ch and last[st[-1]]>i:
                vis.remove(st.pop())
            st.append(ch)
            vis.add(ch)
        return "".join(st)
