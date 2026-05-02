class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        mount = [0]*n

        if n==1:
            return nums[0]
        elif n==2:
            return max(nums)
        
        mount[0] = nums[0]
        mount[1] = max(nums[1] , nums[0])

        for i in range(2,n):
            mount[i] = max(mount[i-2] + nums[i] , mount[i-1])
        return mount[-1]