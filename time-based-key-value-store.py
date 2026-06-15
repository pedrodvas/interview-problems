import bisect

class TimeMap:
    '''
    idea is to create an external dict
    which will use key to point to an internal
    ORDERED list. This list is made of a series of tuples
    with their timestamp and the value for said timestamp.
    This way we can retrieve the key instantly from the 
    dict, and then perform a bin search in the internal
    ordered list in O(lg(n)) time.
    This could be more optimized if before going into the
    internal list an internal dict was accessed, this way
    for all the times that have been added we would have
    a O(K) approach, and it would be O(lg(n)) only for
    when we actually have to search for a non-existent value.
    '''

    def __init__(self):
        self.mapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mapping:
            self.mapping[key].append((timestamp, value))
        else:
            self.mapping[key] = [(timestamp, value)]        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapping or timestamp < self.mapping[key][0][0]:
            return ""
        index_to_insert = bisect.bisect_right(self.mapping[key], timestamp, key=lambda x: x[0])
        return self.mapping[key][index_to_insert-1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)