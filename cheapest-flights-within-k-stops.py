from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flights_graph = defaultdict(list)
        for i in flights:
            curr_src = i[0]
            curr_dst = i[1]
            curr_price = i[2]
            flights_graph[curr_src].append((curr_dst, curr_price))
        
        bfs_queue = deque()

        if k < 0:
            return -1
        for i in flights_graph[src]:
            bfs_queue.append((src, i[0], i[1], k+1))
        
        smallest_prices = [float('inf')]*n

        while bfs_queue:
            curr_flight = bfs_queue.popleft()
            curr_src = curr_flight[0]
            curr_dst = curr_flight[1]
            curr_price = curr_flight[2]
            curr_left = curr_flight[3]
            curr_left = curr_left - 1
            if smallest_prices[curr_dst] < curr_price:
                continue
            smallest_prices[curr_dst] = curr_price
            if curr_dst == dst:
                continue
            if curr_left <= 0:
                continue
            for i in flights_graph[curr_dst]:
                bfs_queue.append((curr_dst, i[0], curr_price+i[1], curr_left))
            

        return smallest_prices[dst] if smallest_prices[dst] != float('inf') else -1

        


if __name__ == "__main__":
    sol = Solution()
    a = sol.findCheapestPrice(n = 4, flights = [[0,1,10],[1,2,10],[2,3,10]], src = 0, dst = 3, k = 1)
    print(a)
