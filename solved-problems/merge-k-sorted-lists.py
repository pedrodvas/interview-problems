import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #initialization
        #base value is a heap with len(lists) spaces
        #to construct the final list, we pop one node for each
        #iteration

        '''
        pseudocode:
        heap = empty
        for i in lists
            push i to heap
        ↓→heap initialized

        final_list = empty
        while heap
            new = pop heap
            if new has next
                push next to heap
            put new after last of final_list
        return final_list
        '''
        print(type(lists))
        print(lists)
        if lists:
            print(type(lists[0]))
            print(lists[0])
        '''
        smallest_node_heap = []
        for i in range(len(lists)):
            curr = lists[i].pop(0)
            print(f"curr is {curr}")
            heapq.heappush(smallest_node_heap, (curr, i))
            #curr will save key, i will save which list it came from
            #we will use this to advance the pointer
        
        return_list = []
        while smallest_node_heap:
            curr = heapq.heappop(smallest_node_heap)
            if lists[curr[1]]:
                to_add = (lists[curr[1]].pop(0), curr[1])
                print(f"will be pushed {to_add}")
                heapq.heappush(smallest_node_heap, to_add)
            
            return_list.append(curr[0])
        
        return return_list

if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeKLists(lists = [[1,4,5],[1,3,4],[2,6]]))'''