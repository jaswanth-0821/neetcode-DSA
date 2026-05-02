class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        def dfs( grid, visited , i , j ):
            nonlocal area
            
            if i<0 or j< 0 or i >=len(grid) or j>=len(grid[0]) or visited[i][j] or grid[i][j]==0:
                return 
           
            visited[i][j] = True
            area +=1
            dfs(grid, visited , i+1 , j)
            dfs(grid, visited , i-1 , j)
            dfs(grid, visited , i , j+1)
            dfs(grid, visited , i , j-1)
            return 
        visited = [[False]*len(grid[0]) for _ in grid]
        max_area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and not visited[i][j]:
                    
                    
                    dfs( grid, visited , i , j )
                    max_area = max(area , max_area)
                    area = 0
                  
        return max_area