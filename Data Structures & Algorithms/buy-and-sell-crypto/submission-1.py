class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Slding window

        l, r = 0, 1
        maxProfit = 0 
        while r < len(prices):
            curProf = prices[r] - prices[l]
            if prices[r] < prices[l]: 
                l = r
                continue
            maxProfit = max(maxProfit, curProf)
            r += 1
        return maxProfit