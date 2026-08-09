class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for pre, crs in prerequisites:
            adj[pre].append(crs)
        visiting = set() 
        def dfs(node):
            if node in visiting: return False 
            if adj[node] == []: return True

            visiting.add(node)
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False 

            adj[node] = []
            visiting.remove(node) 
            return True 

        for course in range(numCourses):
            if not dfs(course):
                return False 

        return True