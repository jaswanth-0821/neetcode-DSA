class Solution:

    def dfs_check(self, board, i,j , word , idx ,visited):

        if idx >= len(word):
            return True
            
        if i < 0 or j <0 or i>= len(board) or j>= len(board[0]) or visited[i][j]:
            return False
       
        if word[idx]!=board[i][j]:
            return False

        visited[i][j]=True
        res =  (
            self.dfs_check(board , i + 1, j , word , idx+1,visited) or 
            self.dfs_check(board , i , j +1 , word , idx+1,visited) or
            self.dfs_check(board , i -1, j , word , idx+1,visited) or 
            self.dfs_check(board , i  , j-1 , word , idx+1,visited)
        )
        visited[i][j]=False
        
        return res


    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True

        visited = [[False]*len(board[0]) for i in range(len(board))]
       
        for i in range(len(board)):
            for j in range(len(board[0])):
              
                if board[i][j]==word[0] and self.dfs_check(board , i, j , word , 0 ,visited):
                    return True
        
        return False
