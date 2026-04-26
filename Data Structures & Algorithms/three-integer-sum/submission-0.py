class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        track = defaultdict(bool)

        list_ = []
        for idx in range(len(nums)):
            for jdx in range(idx+1,len(nums)):
                for kdx in range(jdx+1,len(nums)):
                    i = nums[idx]
                    j = nums[jdx]
                    k = nums[kdx]
                    if i+j+k ==0 and track[tuple(sorted([i,j,k]))]==False:
                        list_.append([i,j,k])
                        track[tuple(sorted([i,j,k]))] = True
        return list_