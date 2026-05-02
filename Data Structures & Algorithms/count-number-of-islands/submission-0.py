class Solution:

    
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs( grid, visited , i , j):
          
            if i<0 or j< 0 or i >=len(grid) or j>=len(grid[0]) or visited[i][j] or grid[i][j]=="0":
                return 
           
            visited[i][j] = True
            dfs(grid, visited , i+1 , j)
            dfs(grid, visited , i-1 , j)
            dfs(grid, visited , i , j+1)
            dfs(grid, visited , i , j-1)
            return 
        visited = [[False]*len(grid[0]) for _ in grid]
        total_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and not visited[i][j]:
                    total_islands +=1
                    dfs( grid, visited , i , j)
                  
        return total_islands