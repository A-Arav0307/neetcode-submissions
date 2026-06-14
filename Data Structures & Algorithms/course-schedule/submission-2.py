class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        visited = set()

        for course, pre in prerequisites:
            graph[pre].append(course)

        def dfs(course):
            if course in visited:
                return False

            if graph[course] == []:
                return True

            visited.add(course)

            for crs in graph[course]:
                if not dfs(crs):
                    return False

            visited.remove(course)
            graph[course] = []
            return True

        for cls in range(numCourses):
            if not dfs(cls):
                return False

        return True