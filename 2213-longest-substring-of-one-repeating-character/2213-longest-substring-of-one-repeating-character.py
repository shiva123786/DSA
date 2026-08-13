class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n=len(s)
        s=list(s)
        tree=[None]*(4*n)
        def combine(a,b):
            lc,rc,pre,suf,best,length=a
            lc2,rc2,pre2,suf2,best2,length2=b
            p=pre
            q=suf2
            if lc==lc2 and pre==length:
                p+=pre2
            if rc==rc2 and suf2==length2:
                q+=suf
            x=max(best,best2)
            if rc==lc2:
                x=max(x,suf+pre2)
            return (lc,rc2,p,q,x,length+length2)
        def build(p,l,r):
            if l==r:
                tree[p]=(s[l],s[l],1,1,1,1)
                return
            m=(l+r)//2
            build(p*2,l,m)
            build(p*2+1,m+1,r)
            tree[p]=combine(tree[p*2],tree[p*2+1])
        def update(p,l,r,i,c):
            if l==r:
                tree[p]=(c,c,1,1,1,1)
                return
            m=(l+r)//2
            if i<=m:
                update(p*2,l,m,i,c)
            else:
                update(p*2+1,m+1,r,i,c)
            tree[p]=combine(tree[p*2],tree[p*2+1])
        build(1,0,n-1)
        ans=[]
        for c,i in zip(queryCharacters,queryIndices):
            update(1,0,n-1,i,c)
            ans.append(tree[1][4])

        return ans