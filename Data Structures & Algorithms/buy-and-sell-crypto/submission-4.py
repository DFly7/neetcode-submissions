class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            curProfit = prices[r] - prices[l]
            print(curProfit)
            if prices[r] < prices[l]:
                l, r = r, r + 1
                continue
            maxProfit = max(maxProfit, curProfit)
            r += 1
        return maxProfit
