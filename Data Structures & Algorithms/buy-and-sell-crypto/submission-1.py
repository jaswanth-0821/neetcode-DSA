class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxi = 0
        for i in range(len(prices)-1,-1,-1):
            maxi = max(maxi,prices[i])
            if prices[i]<maxi:
                profit = max(profit,maxi-prices[i])

        return profit