class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set() 
        self.connected = 0
        adj = {i:[] for i in range(n)}
        for row in range(n):
            for col in range(n):
                if row == col:
                    continue
                if isConnected[row][col] == 1:
                    adj[row].append(col) 

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