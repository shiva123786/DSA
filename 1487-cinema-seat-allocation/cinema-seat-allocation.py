class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows={}
        for r,s in reservedSeats:
            rows[r]=rows.get(r,set())
            rows[r].add(s)
        ans=(n-len(rows))*2
        for seats in rows.values():
            l=seats.isdisjoint({2,3,4,5})
            m=seats.isdisjoint({4,5,6,7})
            r=seats.isdisjoint({6,7,8,9})
            if l and r:
                ans+=2
            elif l or m or r:
                ans+=1
        return ans