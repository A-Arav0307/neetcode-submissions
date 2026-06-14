class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for node, neighbor in edges:
            graph[node].append(neighbor)
            graph[neighbor].append(node) 
        visited = set()
        self.connected = n

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            
        components = 0
        for node in range(n):
            if node not in visited:
                components += 1 
                dfs(node)

        
        return components