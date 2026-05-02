class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

        
        visit = set()

        def  dfs(node , par):
            if node in visit:
                return False
            visit.add(node)
            for n in graph[node]:
                if n==par:
                    continue
                if not dfs(n , node):
                    return False
            return True

        return dfs(0 ,-1) and len(visit) == n
