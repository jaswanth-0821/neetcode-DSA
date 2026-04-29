class Solution:
    def get_idx(self,s):
        return ord(s) - ord("a")

    def check(self,x,y):
        for i , j in zip(x,y):
            if i>j:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        x,y  = [0]*58 , [0]*58
        for  i in t:
            x[self.get_idx(i)] +=1
        
        
        for i in s:
            y[self.get_idx(i)] +=1
        if not self.check(x,y):
            return ""
        y  =  [0]*58
        ans = s
        start_idx = 0 
        end_idx = 0
        while end_idx < len(s):
            
            if x[self.get_idx(s[end_idx])]:
                y[self.get_idx(s[end_idx])]+=1
            
            while self.check(x,y):
                if len(ans) > (( end_idx - start_idx) + 1):
                   
                    ans = s[start_idx : end_idx+1]
                if y[self.get_idx(s[start_idx])]:
                    y[self.get_idx(s[start_idx])] -=1
                start_idx +=1
            
            end_idx +=1    
        
        return ans

