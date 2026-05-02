class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(ans , l ,r ):
            if l==0 and r==0:
                res.append(ans)
                return
            if l>0:
                
                dfs(ans + "(" ,l-1 , r )
            if r>l:
                dfs(ans + ")" , l,r-1)

            return 
        dfs("" , n ,n )
        return res