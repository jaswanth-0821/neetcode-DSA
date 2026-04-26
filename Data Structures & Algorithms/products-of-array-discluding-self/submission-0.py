class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix_prod = [1]*len(nums)
        preffix_prod = [1]*len(nums)
        prod = 1
        for i,n in enumerate(nums):
            if i==0:
                continue
            prod *= nums[i-1]
            preffix_prod[i] = prod
        print(preffix_prod)
        prod =1
        for i in range(len(nums)-1,-1,-1):
            if (i) ==(len(nums)-1):
                continue
            prod *= nums[i+1]
            suffix_prod[i] =prod
        print(suffix_prod)
        return [preffix_prod[i]*suffix_prod[i] for i in range(len(nums))]
        
