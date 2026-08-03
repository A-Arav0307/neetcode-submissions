class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        return n - len(edges)