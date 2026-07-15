class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp=prices[0]
        profit=0
        for i in prices[1:]:
            if bp>i :
                bp=i
            profit=max(profit,i-bp)
        return profit
        