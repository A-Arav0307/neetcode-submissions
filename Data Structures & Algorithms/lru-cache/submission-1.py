class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0) 
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev 

        node.next = self.right
        self.right.prev = node


    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv
        
    def get(self, key: int) -> int:
        if key in self.cache: 
            node = self.cache[key]
            self.remove(node) 
            self.insert(node) 

            return node.value 
        return -1

         
    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]