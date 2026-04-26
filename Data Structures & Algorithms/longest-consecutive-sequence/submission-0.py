class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict_ = defaultdict(bool)
        for i in nums:
            dict_[i]= True

        start_seq = []

        for i in nums:
            if not dict_[i-1]:
                start_seq.append(i)
        
        max_len = 0
        for i in start_seq:
            j=0
            while dict_[i+j]:
                j = j+1
                max_len = max(max_len,j)
        return max_len
