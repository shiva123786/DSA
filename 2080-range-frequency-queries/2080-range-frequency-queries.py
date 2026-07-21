class RangeFreqQuery:

    def __init__(self,arr):
        self.d=defaultdict(list)
        for i,x in enumerate(arr):
            self.d[x].append(i)

    def query(self,left,right,value):
        a=self.d[value]
        return bisect_right(a,right)-bisect_left(a,left)

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)