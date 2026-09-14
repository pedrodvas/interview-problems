class KeyNode:
    def __init__(self, key, value, times_used, next, prev):
        self.key = key
        self.value = value
        self.times_used = times_used
        self.next: KeyNode = next
        self.prev: KeyNode = prev

class LFUCache:
    def __init__(self, capacity: int):
        self.frequency_tiers: dict[int, tuple [KeyNode, KeyNode]] = {}
        self.active_keys: dict[int, KeyNode] = {}
        self.capacity = capacity
        self.smallest_frequency = 0
    
    def get(self, key: int) -> int:
        if key in self.active_keys:
            self.move_up(key)
            return self.active_keys[key].value
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        # if already in, then update value and move up
        # if not:
        #   if capacity not full → just add, reset smallest frequency
        #   if capacity full → remove smallest frequency, add new item, reset smallest frequency
        if key in self.active_keys:
            self.move_up(key)
            self.active_keys[key].value = value
            return
        

    def move_up(self, key):
        to_move = self.active_keys[key]

        #first remove from old frequency tier
        if to_move.prev:
            to_move.prev.next = to_move.next
        if to_move.next:
            to_move.next.prev = to_move.prev

        #add to new one
        new_frequency = to_move.times_used +1

        new_frequency_tail = self.frequency_tiers[new_frequency][1]
        new_frequency_tail.next = to_move
        to_move.prev = new_frequency_tail
        self.frequency_tiers[new_frequency][1] = to_move

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)