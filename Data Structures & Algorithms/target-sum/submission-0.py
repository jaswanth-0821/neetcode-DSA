class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        def dfs(total , i):
            
            if total==target and i== len(nums):
                nonlocal count
                count +=1
            if i>=len(nums):
                return
            dfs(total + nums[i] , i+1)
            dfs(total - nums[i] , i+1)
            return 

        dfs(0 ,0 )
        return count
