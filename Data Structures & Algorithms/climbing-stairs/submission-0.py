class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        df = [0]*(n+1)
        df[0] = 0
        df[1] =1
        df[2] =2
        for i in range(3 ,n+1):
            df[i] = df[i-1] + df[i-2]
        return df[-1]
