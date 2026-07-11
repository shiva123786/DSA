class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g=[[]for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        vis=[False]*n
        ans=0
        def dfs(u):
            vis[u]=True
            nodes=1
            deg=len(g[u])
            for v in g[u]:
                if not vis[v]:
                    a,b=dfs(v)
                    nodes+=a
                    deg+=b
            return nodes,deg
        for i in range(n):
            if not vis[i]:
                nodes,deg=dfs(i)
                if deg==nodes*(nodes-1):
                    ans+=1
        return ans
        