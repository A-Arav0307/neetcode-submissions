class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.courses = []
        adj = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        visiting, visited = set(), set() 

        def dfs(node):
            if node in visiting: return False 
            if adj[node] == []: 
                if node not in visited:
                    self.courses.append(node)
                    visited.add(node)
                return True 

            visiting.add(node) 
            for neighbor in adj[node]:
                if not dfs(neighbor): return False 
                
            adj[node] = []
            if node not in visited: 
                self.courses.append(node) 
                visited.add(node)
            visiting.remove(node)  

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return self.courses

        