class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        ans = []
        res = []
        inputs = [mapping[i] for i in digits]
        def dfs(idx):
            
            if idx>=len(inputs):
                ans.append("".join(res))
                return 
            print(idx)
            for i in inputs[idx]:
                for j in i:
                    res.append(j)
                    dfs(idx+1)
                    res.pop()
            return 
        dfs(0)
        return ans
