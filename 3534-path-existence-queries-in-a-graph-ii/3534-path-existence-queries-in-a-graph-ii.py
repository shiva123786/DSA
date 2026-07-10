class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        a=sorted((v,i)for i,v in enumerate(nums))
        pos=[0]*n
        val=[0]*n
        for i,(v,id) in enumerate(a):
            pos[id]=i
            val[i]=v
        nxt=[0]*n
        j=0
        for i in range(n):
            while j+1<n and val[j+1]-val[i]<=maxDiff:
                j+=1
            nxt[i]=j
        lg=(n).bit_length()
        up=[nxt]
        for _ in range(1,lg):
            p=up[-1]
            up.append([p[p[i]] for i in range(n)])
        ans=[]
        for u,v in queries:
            if u==v:
                ans.append(0)
                continue
            l=pos[u]
            r=pos[v]
            if l>r:
                l,r=r,l
            if nxt[l]==l:
                ans.append(-1)
                continue
            cur=l
            res=0
            for k in range(lg-1,-1,-1):
                if up[k][cur]<r:
                    cur=up[k][cur]
                    res+=1<<k
            if nxt[cur]>=r:
                ans.append(res+1)
            else:
                ans.append(-1)
        return ans