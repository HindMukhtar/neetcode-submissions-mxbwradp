class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}
        self.head = Node(0,0) 
        self.tail = Node(0,0)
        self.head.next = self.tail 
        self.tail.prev = self.head 

    def _removenode(self, node): 
        if node != self.head and node != self.tail: 
            node.prev.next = node.next 
            node.next.prev = node.prev 

            node.next = None
            node.prev = None 

    def _insertmru(self, node): 
        prev = self.tail.prev 
        self.tail.prev = node 
        node.next = self.tail 

        prev.next = node 
        node.prev = prev 

    def get(self, key: int) -> int:
        if key in self.cache: 
            node = self.cache[key]
            if node != self.tail.prev: 
                self._removenode(node)
                self._insertmru(node)

            return self.cache[key].val
        else: 
            return -1 
        
    def put(self, key: int, value: int) -> None:
        if key not in self.cache: 
            if len(self.cache) >= self.capacity: 
                # remove least recently used 
                lru = self.head.next 
                self._removenode(lru)
                del self.cache[lru.key]

            node = Node(key, value)
            self.cache[key] = node    
        else: 
            node = self.cache[key]  
            node.val = value  
            self._removenode(node) 
        self._insertmru(node)
