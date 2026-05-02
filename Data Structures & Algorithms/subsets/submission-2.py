class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # answer = []
        # def dfs(nums , temp_list , i):
           
        #     if i> len(nums)-1:   
        #         answer.append(temp_list.copy())
        #         return 
        #     temp_list.append(nums[i])
        #     dfs(nums , temp_list, i+1)
        #     temp_list.pop()
        #     dfs(nums , temp_list, i+1)
        #     return 

        # dfs(nums , [] , 0)

        # return answer

        res = [[]]
        for num in nums:
            res +=[sub + [num] for sub in res]
        return res