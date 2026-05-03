class Solution:
    def isHappy(self, n: int) -> bool:
        cache =set()
        while n!=1 and (n not in cache):
            cache.add(n)
            sumi =0
            for i in str(n):
                sumi += int(i)**2
            
            
            n = sumi
            
        return n==1
