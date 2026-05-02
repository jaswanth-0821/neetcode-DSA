class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()

        graph = [[] for _ in range(n)]
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        def dfs(node ):
            if node in visited:
                return
            
            visited.add(node)
            for adj in graph[node]:
                if adj not in visited:
                    dfs(adj)

            return

        total = 0
        for i in range(n):
            if i not in visited:
                total+=1
                dfs(i)
        return total
        