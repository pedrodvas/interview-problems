class KeyNode:
    def __init__(self, key, value, times_used, next, prev):
        self.key = key
        self.value = value
        self.times_used = times_used
        self.next: KeyNode | None = next
        self.prev: KeyNode | None = prev

    def __repr__(self):
        ret_str = ""
        ret_str += f"key: {self.key}; value: {self.value}; times_used: {self.times_used}\n"
        next_key = self.next.key if self.next else None
        prev_key = self.prev.key if self.prev else None
        ret_str += f"key prev: {prev_key}; key next: {next_key}"
        return ret_str

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
        print(f"adding key: {key}")
        print(f"frequency to remove {self.smallest_frequency}: {frequency_to_remove}")
        item_to_remove = frequency_to_remove[0]
        if item_to_remove:
            if item_to_remove.next:
                item_to_remove.next.prev = None
                item_to_remove.next = None
            if item_to_remove==frequency_to_remove[1]:
                frequency_to_remove[1] = None
            self.active_keys.pop(item_to_remove.key)

        new = self.active_keys[key] = KeyNode(key, value, 0, None, None)
        self.move_up(new.key)
        self.smallest_frequency = 1
        return

    def __repr__(self):
        ret_str = "=============="
        for i in self.active_keys:
            ret_str += "\n" + str(self.active_keys[i])

        return ret_str

    def move_up(self, key):
        to_move = self.active_keys[key]

        #first remove from old frequency tier
        if to_move.prev:
            to_move.prev.next = to_move.next
        elif to_move.times_used != 0:
            self.frequency_tiers[to_move.times_used][0] = to_move.next
        if to_move.next:
            to_move.next.prev = to_move.prev
        elif to_move.times_used != 0:
            self.frequency_tiers[to_move.times_used][1] = to_move.prev

        if to_move.times_used != 0 and self.frequency_tiers[to_move.times_used][1] == None:
            self.smallest_frequency += 1
        #add to new one
        to_move.times_used += 1
        new_frequency = to_move.times_used

        if new_frequency not in self.frequency_tiers:
            self.frequency_tiers[new_frequency] = [None, None]
        new_frequency_head = self.frequency_tiers[new_frequency][0]
        if not new_frequency_head:
            self.frequency_tiers[new_frequency][0] = to_move
        
        new_frequency_tail = self.frequency_tiers[new_frequency][1]
        if new_frequency_tail:
            new_frequency_tail.next = to_move
        to_move.prev = new_frequency_tail
        to_move.next = None
        self.frequency_tiers[new_frequency][1] = to_move


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    sol = LFUCache(2)
    sol.put(1, 1)
    sol.put(2, 2)
    sol.get(1)
    sol.put(3, 3)
    sol.get(2)
    sol.get(3)
    sol.put(4, 4)
    print(sol.active_keys)
    sol.get(1)
    sol.get(3)
    sol.get(4)