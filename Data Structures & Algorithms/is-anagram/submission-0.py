class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for i in s:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for i in t:
            if i not in count:
                return False
            else:
                count[i]-=1

        for key, value in count.items():
            if value:
                return False
        
        return True