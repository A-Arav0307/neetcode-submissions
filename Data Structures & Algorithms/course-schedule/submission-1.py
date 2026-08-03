class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        visited = set()
        def dfs(courses):
            course2 = courses[0]
            course1 = courses[1]
            if course1 not in graph:
                graph[course1] = []
            graph[course1].append(course2)

            visited.add(course1)
            
            if course2 in visited: 
                return False 

            if course2 in graph:
                if course1 in graph[course2]:
                    return False 

            return True 


        for prerequisite in prerequisites:
            if dfs(prerequisite) == False:
                return False

        return True 
