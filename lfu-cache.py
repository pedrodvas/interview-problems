from collections import deque

class LinkedNode:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None

    def pop_head(self):
        old = self
        curr = self.next
        curr.prev = None
        return old.val, curr

    def remove(self):
        previous = self.prev
        print(f"previous value: {previous}")
        next = self.next
        print(f"next value: {next}")


        if next:
            next.prev = previous
        if previous:
            previous.next = next

    def add_new_tail_value(self, new_val):
        self.next = LinkedNode(new_val)
        self.next.prev = self
        return self.next

    def add_new_tail_node(self, new_node):
        self.next = new_node
        new_node.prev = self
        return self.next

    def print_to_tail(self):
        curr = self
        while curr != None:
            print(f"↓ val: {curr.val}")
            print(f"↓")
            curr = curr.next
        print("Tail!")

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
    that is what AI is recommending. Inside each frequency, we
    store a linked list by recency. This way we know which key
    to delete when a critical put is used.
    '''
    def __init__(self, capacity: int):
        self.per_item_count_dict = {}
        # ↑ each item (1,2,3,4...) will point to a linked list
        #which stores the keys used that many times.
        #it will be (head, tail)
        self.smallest_frequency = None
        self.capacity = capacity
        self.active_keys = {}
        #↑ allows O(1) access to values, instead of searching through
        # the frequency counter dict. Also has to point to 
        #its space in per_item_count_dict, to allow for updating
        #when using put.
        #also has counter for time in its tuple
        

    def get(self, key: int) -> int:
        if key in self.active_keys:
            value = self.active_keys[key][0]
            ref_counter_dict = self.active_keys[key][1]
            times_used = self.active_keys[key][2]+1
            

        

    def put(self, key: int, value: int) -> None:
        if key in self.active_keys:
            self.active_keys[key][0] = value
            ref_counter_dict = self.active_keys[key][1]
            times_used = self.active_keys[key][2]
            self.active_keys[key][1] = self.move_up(ref_counter_dict, times_used) #check if needed

        if key not in self.active_keys:
            #remove least used and add this new key
            self.per_item_count_dict[self.smallest_frequency].pop_head()
            self.active_keys[key] = (value, None, 1)

    def move_up(self, ref_counter_dict, times_used):
        #use to move a key upwards in frequency
        frequency_to_remove = self.per_item_count_dict[times_used]
        frequency_to_add = self.per_item_count_dict[times_used+1]

        #remove item
        ref_counter_dict.remove()
        frequency_to_add[1].add_new_tail_node(ref_counter_dict)
        return ref_counter_dict


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    ""
    print(f"testing linked list implementation")
    head = tail = LinkedNode(1)
    head.print_to_tail()
    tail = tail.add_new_tail_value(2)
    head.print_to_tail()
    tail = tail.add_new_tail_value(3)
    head.print_to_tail()

    tail = tail.add_new_tail_value(4)
    tail = tail.add_new_tail_value(5)
    sixth = tail = tail.add_new_tail_value(6)
    tail = tail.add_new_tail_value(7)
    head.print_to_tail()
    popped, head = head.pop_head()
    print(f"popped value is {popped}")
    popped, head = head.pop_head()
    print(f"popped value is {popped}")
    popped, head = head.pop_head()
    print(f"popped value is {popped}")

    sixth.remove()
    print(f"removed six from linked list")
    print(f"new lnked list is:")
    head.print_to_tail()

    new_node = LinkedNode(8)
    tail = tail.add_new_tail_node(new_node)
    head.print_to_tail()