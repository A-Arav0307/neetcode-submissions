class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        #[([0, 1], -0.5), ([1, 2], -0.5), ([0, 2], -0.2)]]
        adj = {i:[] for i in range(n)}
        max_prob = []
        for i in range(len(edges)):
            start, end = edges[i]
            prob = succProb[i]
            adj[start].append((end, prob))
            

        new_prob = [-prob for prob in succProb]
        heap = [ [-1, start_node] ]

        while heap:
            negProb, node = heapq.heappop(heap)
            prob = -negProb
            if node == end_node:
                max_prob.append(prob)
            for neighbor, probability in adj[node]:
                heapq.heappush(heap, (prob * -probability, neighbor))

        return max(max_prob) if max_prob else 0.0