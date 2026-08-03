class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i:[] for i in range(n)}
        for node, neighbor in edges:
            graph[node].append(neighbor)
            graph[neighbor].append(node)
        visited = set()
        
        def dfs(node, parent):
            if graph[node] == []:
                return True 

            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                new = dfs(neighbor, node)
                if not new:
                    return False
            
            return True 

        return dfs(0, -1)
            