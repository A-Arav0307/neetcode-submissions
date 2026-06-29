class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n) }
        for u, v in edges:
            adj[u].append(v) 
        parent = list(range(n))
        connected = n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(n1, n2):
            root_a, root_b = find(n1), find(n2)
            if root_a == root_b:
                return False 

            parent[root_b] = root_a
            return True
        
        for u, v in edges:
            if union(u, v):
                connected -= 1

        return connected

        