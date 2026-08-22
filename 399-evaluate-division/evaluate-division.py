class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(list)
        
        for (a,b),v in zip(equations,values):
            graph[a].append((b,v))
            graph[b].append((a,1/v))

        def dfs(node,target,visited,value):
            if node==target:
                return value
            visited.add(node)
            for nei,w in graph[node]:
                if nei not in visited:
                    ans=dfs(nei,target,visited,value*w)
                    if ans!=-1:
                        return ans
            return -1
        ans=[]
        for a,b in queries:
            if a not in graph or b not in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(a,b,set(),1.0))
        return ans