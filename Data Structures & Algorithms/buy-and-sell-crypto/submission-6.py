class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, maxProfit = 0, 0

        for r in range(1, len(prices)):
            
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
        return maxProfit
