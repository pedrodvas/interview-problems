class LRUCache:
    '''
    has to deal with data. Will have
    capacity or less keys in it. If a put
    is used when capacity is max, then the 
    key which was used less recently will be deleted
    to put the new one

    idea1: linked list, used keys will be put at the 
    front. We remove element from the back. However accessing
    would be done in O(n)

    idea2: minHeap, for ordering done with time of use.
    If we have to add a new key then the heap is popped.
    Slighly worse then first idea, removing is O(lgn),
    while the first one is both K in adding or removing. 
    Acessing also would not be trivial, probably done at best 
    in O(n)
    '''

    def __init__(self, capacity: int):
        self.history_head = LinkedListNode("head", 22)
        # most recent
        self.history_tail = LinkedListNode("tail", 22)
        # oldest
        self.history_head.prev = self.history_tail
        self.history_tail.next = self.history_head
        self.access_cache = {}
        self.max_capacity = capacity
        self.curr_capacity = 0

    def get(self, key: int) -> int:
        #access cache to get list addr
        head = self.history_head
        head.all_print_prev()
        if key in self.access_cache:
            node_to_access = self.access_cache[key]
            node_to_access.next.prev = node_to_access.prev
            node_to_access.prev.next = node_to_access.next
            
            node_to_access.prev = self.history_head.prev
            node_to_access.next = self.history_head
            self.history_head.prev = node_to_access
            node_to_access.prev.next = node_to_access
            return node_to_access.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        head = self.history_head
        head.all_print_prev()

        if key in self.access_cache:
            self.access_cache[key].value = value

            node_to_access = self.access_cache[key]
            node_to_access.next.prev = node_to_access.prev
            node_to_access.prev.next = node_to_access.next
            
            node_to_access.prev = self.history_head.prev
            node_to_access.next = self.history_head
            self.history_head.prev = node_to_access
            node_to_access.prev.next = node_to_access

        elif self.curr_capacity == self.max_capacity:
            # remove 1, then put the other
            oldest = self.history_tail.next
            self.history_tail.next = oldest.next
            oldest.next.prev = self.history_tail
            del self.access_cache[oldest.key]

            new_node = LinkedListNode(key, value)
            new_node.next = self.history_head
            new_node.prev = self.history_head.prev
            
            self.history_head.prev = new_node
            new_node.prev.next = new_node

            self.access_cache[key] = new_node

        else:
            # only put the other one
            new_node = LinkedListNode(key, value)
            new_node.next = self.history_head
            new_node.prev = self.history_head.prev
            
            self.history_head.prev = new_node
            new_node.prev.next = new_node

            self.access_cache[key] = new_node
            self.curr_capacity += 1

class LinkedListNode:
    def __init__(self, key, value: int):
        self.prev = None
        self.key = key
        self.value = value
        self.next = None
    
    def all_print_prev(self):
        return
        curr = self
        while curr:
            print(f"key: {curr.key} | value: {curr.value}")
            curr = curr.prev
        print(f"=====finished=======")
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)  # cache is {1=1}
    lru_cache.put(2, 2)  # cache is {1=1, 2=2}
    lru_cache.get(1)     # return 1
    lru_cache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    lru_cache.get(2)     # returns -1 (not found)
    print("problem after here\n==========")
    lru_cache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lru_cache.get(1)     # return -1 (not found)
    lru_cache.get(3)     # return 3
    lru_cache.get(4)     # return 4
