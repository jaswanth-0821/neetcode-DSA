class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
    
        ans = []
        temp_list =[]
        def dfs(nums , idx ):
           
            if idx>=len(nums):
                ans.append(temp_list[:])
                return
            temp_list.append(nums[idx])
            dfs(nums , idx+1)
            temp_list.pop()

            while (idx+1) < len(nums) and nums[idx]==nums[idx+1]:
                idx = idx+1
            dfs(nums, idx+1)
            return
      
        dfs(nums , 0)
        return ans