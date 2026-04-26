class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i]+=1

        list_ = list(count.keys())
        list_ = sorted(list_, key=lambda i: count[i],reverse=True)
        return list_[:k]