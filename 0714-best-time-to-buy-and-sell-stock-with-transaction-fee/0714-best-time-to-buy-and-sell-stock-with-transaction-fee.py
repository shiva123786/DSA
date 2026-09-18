class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        cash=0
        hold=-prices[0]
        for p in prices[1:]:
            cash=max(cash,hold+p-fee)
            hold=max(hold,cash-p)
        return cash