class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        q=[]
        for i,(p,s) in enumerate(queries):
            q.append((s,p,i))
        q.sort(reverse=True)
        rooms.sort(key=lambda x:x[1],reverse=True)
        sl=SortedList()
        ans=[-1]*len(queries)
        j=0
        for s,p,i in q:
            while j<len(rooms) and rooms[j][1]>=s:
                sl.add(rooms[j][0])
                j+=1
            if not sl:
                continue
            k=sl.bisect_left(p)
            best=None
            if k<len(sl):
                best=sl[k]
            if k>0:
                x=sl[k-1]
                if best is None or abs(x-p)<=abs(best-p):
                    best=x
            ans[i]=best
        return ans