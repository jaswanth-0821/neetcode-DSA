class Solution:
    def check_dict(self,dict_):
        for k,v in dict_.items():
            if v>1:
                return True
        return False
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_ = defaultdict(int)
        max_len = 0
        i=0
        j =0
        while j<len(s):
            dict_[s[j]]+=1
            while self.check_dict(dict_):
                dict_[s[i]] -=1
                i +=1
            max_len = max(max_len , (j-i)+1)
            j +=1
        return max_len