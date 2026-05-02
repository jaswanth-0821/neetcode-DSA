class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 1e9
        dp  = [INF]*(amount+1)

        dp[0] = 0

        for i in range(amount +1):
            for c in coins:
                if c<=i:
                    dp[i] = min(1 + dp[i-c] , dp[i])
        return dp[-1] if dp[-1]<=amount else -1
