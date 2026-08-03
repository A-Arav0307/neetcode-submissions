class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = list(range(numCourses))
        self.res = []
        visiting = set()
        adj = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[pre].append(course)
        
        def dfs(node):
            if node in visiting:
                return False
            if adj[node] == []:
                self.res.append(node)
                return True 

            visiting.add(node) 
            self.res.append(node) 
            for neighbor in adj[node]:
                dfs(neighbor)
            
            
            adj[node] = []
            
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return self.res