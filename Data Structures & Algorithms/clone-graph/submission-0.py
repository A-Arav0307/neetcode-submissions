"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        from collections import deque
        if not node: 
            return None 
        graph_list = {}

        graph_list[node] = Node(node.val)
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                 
                if neighbor not in graph_list:
                    queue.append(neighbor)
                    graph_list[neighbor] = Node(neighbor.val)

                graph_list[curr].neighbors.append(graph_list[neighbor])

        return graph_list[node]


