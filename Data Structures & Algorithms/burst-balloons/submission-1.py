class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def dfs(nums  ):
            if len(nums)==2:
                return 0
            if tuple(nums) in dp:
                return dp[tuple(nums)]
            max_sum = 0
            for i in range(1, len(nums)-1):
                sumi = nums[i-1]*nums[i]*nums[i+1]
                max_sum = max(sumi + dfs(nums[:i] + nums[i+1:]) , max_sum)
            dp[tuple(nums)] = max_sum
            return dp[tuple(nums)]
        return dfs(nums) 
                