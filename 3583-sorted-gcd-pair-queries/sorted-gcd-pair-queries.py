class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        m=max(nums)
        freq=[0]*(m+1)
        for x in nums:
            freq[x]+=1
        cnt=[0]*(m+1)
        for g in range(1,m+1):
            c=0
            for j in range(g,m+1,g):
                c+=freq[j]
            cnt[g]=c*(c-1)//2
        exact=[0]*(m+1)
        for g in range(m,0,-1):
            exact[g]=cnt[g]
            for j in range(g*2,m+1,g):
                exact[g]-=exact[j]
        pre=[0]*(m+1)
        for i in range(1,m+1):
            pre[i]=pre[i-1]+exact[i]
        ans=[]
        for q in queries:
            l,r=1,m
            while l<r:
                mid=(l+r)//2
                if pre[mid]>q:
                    r=mid
                else:
                    l=mid+1
            ans.append(l)
        return ans