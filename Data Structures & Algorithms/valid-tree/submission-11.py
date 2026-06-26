class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        self.parent = list(range(n))

        def find(x):
            while x != self.parent[x]:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x

        def union(n1, n2):
            root_a, root_b = find(n1), find(n2) 

            if root_a == root_b:
                return False
            
            self.parent[root_b] = self.parent[root_a]

            return True

        for a, b in edges:
            if not union(a,b):
                return False

        root = find(0)
        for i in range(n):
            if find(i) != root:
                return False

        return True 
