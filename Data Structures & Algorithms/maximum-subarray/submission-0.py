class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        sumi = nums[0]
        for i in nums[1:]:
            if sumi>=0:
                sumi += i
            else:
                sumi = i
            
            ans = max(sumi , ans)
        return ans     
