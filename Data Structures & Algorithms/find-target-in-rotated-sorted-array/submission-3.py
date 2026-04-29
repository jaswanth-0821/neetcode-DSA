class Solution:
    def search_point(self, nums):
        l =0
        r = len(nums)-1
        while(l<r):
            m = l +(r-l)//2

            if nums[m]<nums[r]:
                r = m
            else:
                l = m+1
        return r

    def binary_search(self,nums , target , delta):
        l = 0
        r = len(nums)-1
        while(l<=r):
           
            m = l + (r-l)//2
           
            if nums[(m + delta)% len(nums)]==target:
                return (m + delta)%len(nums)
            if nums[(m + delta)% len(nums)]<target:
                l = m+1
            else:
                r = m-1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        point = self.search_point(nums)
        print(point)
        return self.binary_search(nums, target , point) 