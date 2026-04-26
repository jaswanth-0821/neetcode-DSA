class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        s = s.replace(" ","")
        valid = [chr(ord("a") + i) for i in range(26)] + [str(i) for i in range(10)] + [" "]
        # print(valid)

        i = 0
        j = len(s)-1
        while i<j:
            
            while i<j and (s[i] not in valid):
                i = i+1
            while i<j and (s[j] not in valid):
                j = j-1
            # print(s[i],s[j])
            if i==j:
                return True
            
            if s[i]!=s[j]:
                return False
            i = i+1
            j = j-1
        return True