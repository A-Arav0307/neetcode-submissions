class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        components = 0
        visited = set()
        for u, v in edges: 
            adj[u].append(v) 
            adj[v].append(u) 

        def dfs(node):
            for neighbor in adj[node]: 
                if neighbor not in visited:
                    visited.add(neighbor) 
                    dfs(neighbor) 

        for i in range(n):
            if i not in visited: 
                visited.add(i)
                dfs(i) 
                components += 1

        return components 



        