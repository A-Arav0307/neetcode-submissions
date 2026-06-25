class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = list(range(numCourses))
        self.res = []
        visiting, visited = set(), set()
        adj = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)
        
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True

            visiting.add(node)
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            visited.add(node)
            visiting.remove(node)
            self.res.append(node)

            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        return self.res