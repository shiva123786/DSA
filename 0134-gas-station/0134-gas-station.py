class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return-1
        t=s=0
        a=0
        for i in range(len(gas)):
            t+=gas[i]-cost[i]
            if t<0:
                t=0
                a=i+1
        return a