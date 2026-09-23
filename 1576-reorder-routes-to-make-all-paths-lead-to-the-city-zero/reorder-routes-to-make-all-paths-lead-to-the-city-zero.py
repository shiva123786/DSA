class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        g=[[] for _ in range(n)]
        for a,b in connections:
            g[a].append((b,1))
            g[b].append((a,0))
        ans=0
        st=[(0,-1)]
        while st:
            u,p=st.pop()
            for v,c in g[u]:
                if v!=p:
                    ans+=c
                    st.append((v,u))
        return ans