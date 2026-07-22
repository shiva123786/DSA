class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        pos=SortedList([-1,len(s)])
        for t,i in enumerate(order):
            j=pos.bisect(i)
            k-=(i-pos[j-1])*(pos[j]-i)
            pos.add(i)
            if k<=0:
                return t
        return -1