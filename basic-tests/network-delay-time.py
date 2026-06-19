import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        using modified bfs only walking 1 weight at a time
        would work with good asymptotic growth, but with too
        big constants.
        
        the better solution is just using dijsktra
        '''
        graph_dict = defaultdict(list)
        closest_heap = []
        min_times = (n+1)*[None]
        min_times[k] = 0
        for i in range(len(times)):
            origin = times[i][0]
            time = times[i][2]
            destiny = times[i][1]
            graph_dict[origin].append((time, origin, destiny))

        for i in range(len(graph_dict[k])):
            heapq.heappush(closest_heap, graph_dict[k][i])
        
        #the heap should store the accumullated time, and not edge only
        #with the above change, we can also implement another optimization
        visited = (n+1)*[False]
        while closest_heap:
            curr_edge = heapq.heappop(closest_heap)
            time = curr_edge[0]
            origin = curr_edge[1]
            destiny = curr_edge[2]
            if visited[destiny] == True:
                continue
            visited[destiny] = True
            if min_times[destiny] == None or min_times[destiny] > time:
                min_times[destiny] = time
            
                #forgot to add new nodes
                for i in range(len(graph_dict[destiny])):
                    to_add_time, to_add_origin, to_add_destiny = graph_dict[destiny][i]
                    to_add_time += time #sum with time to reach origin
                    heapq.heappush(closest_heap, (to_add_time, to_add_origin, to_add_destiny))
        
        
        if None in min_times[1:]:
            return -1
        return max(min_times[1:])
            
if __name__ == "__main__":
    sol = Solution()
    print(sol.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
    print(sol.networkDelayTime(times = [[1,2,1],[2,1,3]], n = 2, k = 2))
