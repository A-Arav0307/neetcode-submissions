import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_list = []
        distances = []
        for point in points: 
            x,y = point[0], point[1]
            distance = x**2 + y**2
            distances.append([-distance, x, y])

        
        heapq.heapify(distances)
        
        while len(distances) > k:
            heapq.heappop(distances)
        for x,y,z in distances:
            points_list.append([y,z])

        return points_list
