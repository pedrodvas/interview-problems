from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flights_graph = defaultdict(list)
        for i in flights:
            curr_src = i[0]
            curr_dst = i[1]
            curr_price = i[2]
            flights_graph[curr_src].append((curr_dst, curr_price))
        
        #here the graph is already initialized
        #now I am going to prepare the variables
        #that are going to be used in the modified BFS
        #in the initial stack, I will put the neighbors to src
        bfs_queue = deque()
        #bfs elements will be (src, dst, price)
        #we need to have src to measure how many
        #flights were already taken before we got there
        if k < 0:
            return -1
        for i in flights_graph[src]:
            bfs_queue.append((src, i[0], i[1], k+1))
        
        #you don't have to worry about going back to a point you've gone
        #before, because, if this new path is the new smallest one, the bfs will
        #eventually get to your destiny with the new cheapest combination

        #now we should start iterating through each node
        #using the bfs, and ignoring the nodes that have 
        #no trips left. The amount of trips left will be accessed
        #by the flights_left list.

        smallest_prices = [float('inf')]*n

        while bfs_queue:
            curr_flight = bfs_queue.popleft()
            curr_src = curr_flight[0]
            curr_dst = curr_flight[1]
            curr_price = curr_flight[2]
            curr_left = curr_flight[3]
            curr_left = curr_left - 1
            if curr_left <= 0:
                continue
            if smallest_prices[curr_dst] < curr_price:
                continue
            smallest_prices[curr_dst] = curr_price
            if curr_dst == dst:
                continue
            for i in flights_graph[curr_dst]:
                bfs_queue.append((curr_dst, i[0], curr_price+i[1], curr_left))
            

        return smallest_prices[dst] if smallest_prices[dst] != float('inf') else -1

        


if __name__ == "__main__":
    sol = Solution()
    a = sol.findCheapestPrice(n = 4, flights = [[0,1,10],[0,2,50],[1,2,10],[2,3,10]], src = 0, dst = 3, k = 1)
    print(a)
