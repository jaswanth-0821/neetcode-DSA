from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = defaultdict(bool)
        for i in nums:
            if store[i]:
                return True
            store[i]=True
        return False
        