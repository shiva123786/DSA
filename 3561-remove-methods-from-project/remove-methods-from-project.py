class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(n)]
        for u,v in invocations:
            graph[u].append(v)
        bad=[False]*n
        def dfs(u):
            bad[u]=True
            for v in graph[u]:
                if not bad[v]:
                    dfs(v)

        dfs(k)

        for u,v in invocations:
            if not bad[u] and bad[v]:
                return [i for i in range(n)]
        ans=[]
        for i in range(n):
            if not bad[i]:
                ans.append(i)
        return ans