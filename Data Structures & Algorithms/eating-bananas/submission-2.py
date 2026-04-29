import math
class Solution:
    def check(self,piles , h, target):
        time = [math.ceil(p/target) for p in piles]
        return sum(time)<=h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      
        l = 1
        r = max(piles)
        res = r
        while(l<=r):
            m = (l+r) // 2

         
            if self.check(piles, h , m):
                res = m
                r = m-1
            else:
                l = m+1
       
        return res