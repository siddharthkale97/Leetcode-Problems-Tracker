'''
146. LRU Cache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
'''

class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mapk = {}
        self.right, self.left = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next =  nxt.prev = node
        node.next, node.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key in self.mapk:
            self.remove(self.mapk[key])
            self.insert(self.mapk[key])
            return self.mapk[key].value
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.mapk:
            self.remove(self.mapk[key])
        self.mapk[key] = Node(key, value)
        self.insert(self.mapk[key])
        
        if len(self.mapk) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.mapk[lru.key]
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
'''
Runtime: 928 ms, faster than 51.10% of Python3 online submissions for LRU Cache.
Memory Usage: 76.3 MB, less than 25.54% of Python3 online submissions for LRU Cache.
'''