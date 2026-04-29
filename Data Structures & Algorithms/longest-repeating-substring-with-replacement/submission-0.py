class Solution:
    def check(self,x):
        values = list(x.values())
        values = [v for v in values if v>0]
        if not values:
            return -1
        if len(values)==1:
            return -1
        
        return sum(values) - max(values)
        
    def characterReplacement(self, s: str, k: int) -> int:
        x = defaultdict(int)
        i =0
        j = 0
        res = 1
        while  j<len(s):
            x[s[j]] +=1
            while i<j and self.check(x ) >k:
                
                x[s[i]] -=1
                i = i +1
            
            
            res = max(res , ( j-i)+1)
           
            j = j+1
            

        return res