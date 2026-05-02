class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cmax , cmin = 1,1

        for num in nums:
            cmin , cmax = min(cmax*num , cmin*num ,num ), max(num*cmin , num*cmax, num)
            res= max(res , cmax)
        return res
            