class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(n1, n2):
            root1 = find(n1)
            root2 = find(n2)
            if root1 == root2:
                return False
            
            parent[root2] = root1
            return True

        
        for p, node in edges:
            if not union(p, node):
                return [p, node]

        