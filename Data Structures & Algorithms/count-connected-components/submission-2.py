class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        visited = set()
        self.connected = 0

        def dfs(node):
            if node in visited:
                return False 
            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor) 
            return True

        for i in range(n): 
            if dfs(i):
                self.connected += 1
        return self.connected