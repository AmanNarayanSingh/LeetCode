class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x=float('inf')
        sell=0
        for i in prices:
            x=min(x,i)
            sell=max(sell,i-x)
        return sell