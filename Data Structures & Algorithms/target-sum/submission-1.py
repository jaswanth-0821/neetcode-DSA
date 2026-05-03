class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        dp = {}
        def dfs(total , i):
            if (total , i) in dp:
                return dp[(total  ,i )]
            if  i== len(nums):
                return 1 if total==target else 0
            
            dp[(total , i)] = dfs(total + nums[i] , i+1) + dfs(total - nums[i] , i+1)
            return dp[(total , i)]

        count  = dfs(0 ,0 )
        return count
