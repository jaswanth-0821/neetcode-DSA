class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        s = s.replace(" ","")
        valid = [chr(ord("a") + i) for i in range(26)] + [str(i) for i in range(10)] + [" "]
        
        s= [i for i in s if i in valid]
        
        i =0 
        j = len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            i = i+1
            j = j-1
        return True