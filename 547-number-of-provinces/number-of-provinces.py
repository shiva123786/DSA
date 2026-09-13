class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        seen=set()
        ans=0
        def dfs(i):
            seen.add(i)
            for j in range(n):
                if isConnected[i][j] and j not in seen:
                    dfs(j)
        for i in range(n):
            if i not in seen:
                ans+=1
                dfs(i)
        return ans