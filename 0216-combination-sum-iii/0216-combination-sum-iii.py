class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans=[]
        def dfs(i,path,s):
            if len(path)==k:
                if s==n:
                    ans.append(path[:])
                return
            for x in range(i,10):
                if s+x>n:
                    break
                path.append(x)
                dfs(x+1,path,s+x)
                path.pop()
        dfs(1,[],0)
        return ans