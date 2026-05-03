class Solution:
    def countBits(self, n: int) -> List[int]:
        results = []
        for nn in range(n+1):
            res = 0
            for i in range(32):
                if (1 << i) & nn:
                    res += 1
            results.append(res)
        return results