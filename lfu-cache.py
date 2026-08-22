class LFUCache:
    '''
    to solve this problem we will
    have a counter for each one of the keys. 
    We have to remeber that all operations should
    increase the counter of the key, being it getting
    the value of the key, or updating it through a put.

    What can we do to ensure o1 operations?
    If we use a linked list, then at worst each key
    will have to skip through all the other keys that have
    the same counter as itself. This approaches o1 strongly, due
    to the low likelihood of sharing counters

    If instead we use a heap, then we would run essentially
    into the same problem. However, here updating a value
    would make our key move less due to the tree like structure
    of the heap. However, remotions would be way more expensive
    because of the extra movements when heapifying.

    You thought using a hash for frequencies wouldn't work, but
    that is wah AI is recommending. Inside each frequency, we
    store a linked list by recency. This way we know which key
    to delete when a critical put is used.
    '''
    def __init__(self, capacity: int):
        

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)