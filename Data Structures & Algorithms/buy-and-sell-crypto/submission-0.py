class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 1
        maxprofit = 0
        while(right < len(prices)):
            profit = prices[right] - prices[left]
            if (profit > 0):
                maxprofit = max(profit, maxprofit)
            else:
                left = right
            right += 1
        return maxprofit