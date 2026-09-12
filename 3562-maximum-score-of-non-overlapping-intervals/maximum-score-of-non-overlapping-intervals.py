class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        a=sorted((l,r,w,i) for i,(l,r,w) in enumerate(intervals))
        @lru_cache(None)
        def dp(i,k):
            if i==len(a) or k==0:
                return 0,()
            skip=dp(i+1,k)
            l,r,w,idx=a[i]
            j=bisect_right(a,(r,10**20,10**20,10**20))
            x=dp(j,k-1)
            take=(w+x[0],tuple(sorted((idx,)+x[1])))
            return take if take[0]>skip[0] or take[0]==skip[0] and take[1]<skip[1] else skip
        return list(dp(0,4)[1])