class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n=len(arr)
        odd=[False]*n
        even=[False]*n
        odd[-1]=even[-1]=True
        sd=SortedDict()
        sd[arr[-1]]=n-1
        ans=1
        for i in range(n-2,-1,-1):
            j=sd.bisect_left(arr[i])
            if j<len(sd):
                odd[i]=even[sd.peekitem(j)[1]]
            j=sd.bisect_right(arr[i])-1
            if j>=0:
                even[i]=odd[sd.peekitem(j)[1]]
            if odd[i]:
                ans+=1
            sd[arr[i]]=i
        return ans
        