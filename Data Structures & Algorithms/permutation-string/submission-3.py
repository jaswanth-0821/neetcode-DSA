class Solution:
    def str_idx(self,s):
        return ord(s) - ord("a")
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x ,y = [0]*26 ,  [0]*26
        if len(s2)<len(s1):
            return False
        for s in s1:
            x[self.str_idx(s)] +=1
        
        for idx in range(len(s1)):
            y[self.str_idx(s2[idx])] +=1
        if x==y:
            return True
        for idx in range(len(s1) , len(s2)):
            
            y[self.str_idx(s2[idx])] +=1
            if y[self.str_idx(s2[idx - len(s1)])]:
                y[self.str_idx(s2[idx - len(s1)])] -=1
           
            if x==y:
                return True
            
        return False
        