class Solution:
    def resultArray(self,nums,k,queries):
        n=len(nums)
        tree=[None]*(4*n)
        def merge(a,b):
            p=a[0]*b[0]%k
            c=a[1][:]
            for x in range(k):
                c[a[0]*x%k]+=b[1][x]
            return p,c
        def build(o,l,r):
            if l==r:
                c=[0]*k
                c[nums[l]%k]=1
                tree[o]=(nums[l]%k,c)
                return
            m=(l+r)//2
            build(o*2,l,m)
            build(o*2+1,m+1,r)
            tree[o]=merge(tree[o*2],tree[o*2+1])
        def update(o,l,r,i,v):
            if l==r:
                c=[0]*k
                c[v%k]=1
                tree[o]=(v%k,c)
                return
            m=(l+r)//2
            if i<=m:
                update(o*2,l,m,i,v)
            else:
                update(o*2+1,m+1,r,i,v)
            tree[o]=merge(tree[o*2],tree[o*2+1])
        def query(o,l,r,ql,qr):
            if ql<=l and r<=qr:
                return tree[o]
            m=(l+r)//2
            if qr<=m:
                return query(o*2,l,m,ql,qr)
            if ql>m:
                return query(o*2+1,m+1,r,ql,qr)
            return merge(query(o*2,l,m,ql,qr),query(o*2+1,m+1,r,ql,qr))
        build(1,0,n-1)
        ans=[]
        for i,v,s,x in queries:
            update(1,0,n-1,i,v)
            ans.append(query(1,0,n-1,s,n-1)[1][x])
        return ans