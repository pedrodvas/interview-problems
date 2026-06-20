from collections import defaultdict

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
        flights_left = [None]*n
        flights_left[src] = k
        #in the initial stack, I will put the neighbors to src
        bfs_stack = []
        #bfs elements will be (src, dst, price)
        #we need to have src to measure how many
        #flights were already taken before we got there
        for i in range(len(flights_graph[src])):
            bfs_stack.append((src, flights_graph[src][i][0], flights_graph[src][i][1]))
        
        print(bfs_stack)
        #now we should start iterating through each node
        #using the bfs, and ignoring the nodes that have 
        #no trips left. The amount of trips left will be accessed
        #by the flights_left list.


if __name__ == "__main__":
    sol = Solution()
    sol.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1)
