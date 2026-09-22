class SmallestInfiniteSet:

    def __init__(self):
        self.h=[]
        self.s=set()
        self.cur=1
    def popSmallest(self):
        if self.h:
            x=heapq.heappop(self.h)
            self.s.remove(x)
            return x
        x=self.cur
        self.cur+=1
        return x
    def addBack(self,num):
        if num<self.cur and num not in self.s:
            heapq.heappush(self.h,num)
            self.s.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)