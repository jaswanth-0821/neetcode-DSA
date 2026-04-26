class Solution:
    def check_valid(self,i,track_stack):
        if not track_stack:
            return False
        if track_stack[-1] + i =="{}":
            return True
        if track_stack[-1] + i =="()":
            return True
        if track_stack[-1] + i =="[]":
            return True
        return False
    def isValid(self, s: str) -> bool:

        track_stack = []
        for i in s:
            if i in ["(", "{","["]:
                track_stack.append(i)
            elif self.check_valid(i,track_stack):
                track_stack.pop()
            else:
                return False
        if track_stack:
            return False
        return True