class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indi = {}
        for i,j in enumerate(nums):
            indi[j] = i
        
        for idx,i in enumerate(nums):
            if ((target-i) in indi) and (indi[target - i]!=idx):
                return sorted([indi[target - i],idx])
        return False
