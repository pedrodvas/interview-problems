class KeyNode:
    def __init__(self, key, value, times_used, next, prev):
        self.key = key
        self.value = value
        self.times_used = times_used
        self.next: KeyNode | None = next
        self.prev: KeyNode | None = prev

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
        if len(self.active_keys) < self.capacity:
            new = self.active_keys[key] = KeyNode(key, value, 0, None, None)
            self.move_up(new.key)
            self.smallest_frequency = 1
            return

        #removing oldest with smallest count
        frequency_to_remove = self.frequency_tiers[self.smallest_frequency]
        item_to_remove = frequency_to_remove[0]
        self.active_keys.pop(item_to_remove.key)
        if frequency_to_remove[0].next:
            frequency_to_remove[0].next.prev = None
        frequency_to_remove[0] = frequency_to_remove[0].next

        new = self.active_keys[key] = KeyNode(key, value, 0, None, None)
        self.move_up(new.key)
        self.smallest_frequency = 1
        return

        

    def move_up(self, key):
        to_move = self.active_keys[key]

        #first remove from old frequency tier
        if to_move.prev:
            to_move.prev.next = to_move.next
        if to_move.next:
            to_move.next.prev = to_move.prev

        #add to new one
        new_frequency = to_move.times_used + 1

        new_frequency_head = self.frequency_tiers[new_frequency][0]
        if not new_frequency_head:
            self.frequency_tiers[new_frequency][0] = to_move
        
        new_frequency_tail = self.frequency_tiers[new_frequency][1]
        if new_frequency_tail:
            new_frequency_tail.next = to_move
        to_move.prev = new_frequency_tail
        self.frequency_tiers[new_frequency][1] = to_move


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)