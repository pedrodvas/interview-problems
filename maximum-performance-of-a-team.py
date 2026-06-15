class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        '''
        why would the solution below work?
        Given a list of engineers, their efficiency is limited
        by the lowest one of the group. In that case,
        if we switch any other engineer by one with a higher
        speed we will definetely find a new combination with 
        a higher performance. 
        But can a discarted engineer belong to a group that
        hasn't been analyzed yet? No, because the groups
        efficiency is already defined by the member that
        substituted them. And when talking about speed, if
        it was popped then some other member was able to
        outperform their speed, maximizing the performance
        with the current efficiency.
        '''
        engineer_list = []
        for i in range(len(speed)):
            engineer_list.append(Node(speed[i], efficiency[i]))

        engineer_list.sort(key=lambda x: x.efficiency, reverse=True)
        print(f"engineer list is {engineer_list}\n")

        speeds_sum = 0
        speeds_sum += engineer_list[0].speed
        speeds_heap = MinHeap(engineer_list[0].speed, engineer_list[0].efficiency)
        curr_min_efficiency = engineer_list[0].efficiency
        max_performance = speeds_sum*curr_min_efficiency
        for i in range(1, len(engineer_list)):
            print(f"top now:\n{speeds_heap}")
            print(f"now checking eng: {engineer_list[i]}")
            speeds_sum += engineer_list[i].speed
            speeds_heap.add(engineer_list[i].speed, engineer_list[i].efficiency)
            curr_min_efficiency = engineer_list[i].efficiency

            if speeds_heap.size > k:
                slowest = speeds_heap.pop()
                print(f"removed {slowest}")
                speeds_sum -= slowest.speed

            curr_performance = speeds_sum*curr_min_efficiency
            print(f"curr perf = {speeds_sum} * {curr_min_efficiency}")
            if curr_performance > max_performance:
                max_performance = curr_performance

        print(f"top now:\n{speeds_heap}")
        return max_performance

class MinHeap:
    def __init__(self, speed, efficiency):
        self._list = [Node(speed, efficiency)]
        self.size = 1
    
    def add(self, key, data):
        self._list.append(Node(key, data))
        new_index = len(self._list)-1
        parent_index = self.parent(new_index)      
        while parent_index >= 0 and self._list[new_index].speed < self._list[parent_index].speed:
            self._list[new_index], self._list[parent_index] = self._list[parent_index], self._list[new_index]
            new_index = parent_index
            parent_index = self.parent(new_index)
        self.size += 1
    
    def pop(self)->Node:
        to_remove = 0
        left, right = self.sons(to_remove)
        while self._list[to_remove]:
            if right<len(self._list):
                if self._list[left].speed < self._list[right].speed:
                    self._list[to_remove], self._list[left] = self._list[left], self._list[to_remove]
                    to_remove = left
                else:
                    self._list[to_remove], self._list[right] = self._list[right], self._list[to_remove]
                    to_remove = right
            elif left<len(self._list):
                self._list[to_remove], self._list[left] = self._list[left], self._list[to_remove]
                to_remove = left
            else:
                self.size -= 1
                return self._list.pop(to_remove) #end of the list, node has to be removed
            left, right = self.sons(to_remove)
            

    def parent(self, index: int):
        return (index-1)//2
    
    def sons(self, index: int):
        return 2*index+1, 2*index+2
    
    def __str__(self):
        ret_list = []
        for i in self._list:
            ret_list.append(f"speed: {i.speed} | efficiency: {i.efficiency}\n")

        return "".join(ret_list)

class Node:
    def __init__(self, speed:int, efficiency):
        self.speed = speed
        self.efficiency = efficiency
    
    def __str__(self):
        return f"speed: {self.speed} efficiency: {self.efficiency}"
    
    def __repr__(self):
        return f"({self.speed}, '{self.efficiency}')"


def calculate_performance(speeds, minimum_efficiency):
    total_speed = 0
    for i in range(len(speeds)):
        total_speed += speeds[i]    
    return minimum_efficiency*total_speed

if __name__ == "__main__":
    sol = Solution()
    performance = sol.maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2)
    print(f"max performance is {performance}")