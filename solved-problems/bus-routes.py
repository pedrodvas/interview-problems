from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        paths_graph = defaultdict(list)
        for route in range(len(routes)):
            for curr_stop_index in range(len(routes[route])):
                next_stop_index = (curr_stop_index+1)%len(routes[route])
                print(curr_stop_index)
                paths_graph[routes[route][curr_stop_index]].append((routes[route][next_stop_index], route))
        print(f"paths graph:\n{paths_graph}")

        routes_per_stop = defaultdict(set)
        for route in range(len(routes)):
            for stop in routes[route]:
                routes_per_stop[stop].add(route)
        print(f"routes for each stop:\n{routes_per_stop}")

        route_connection_graph = defaultdict(set)
        for route in range(len(routes)):
            for stop in routes[route]:
                for next_stop in paths_graph[stop]:
                    if next_stop[1] != route:
                        route_connection_graph[route].add(next_stop[1])
        print(f"route connection graph:\n{route_connection_graph}")

        # find the destiny routes
        starting_routes = routes_per_stop[source]
        destiny_routes = routes_per_stop[target]
        print(f"starting routes is {starting_routes}")
        print(f"destiny routes is {destiny_routes}")
        seen_routes = set()

        bfs_routes_queue = deque()
        for starting_route in starting_routes:
            bfs_routes_queue.append((starting_route, 1))

        while bfs_routes_queue:
            print(f"bfs routes queue:\n{bfs_routes_queue}")
            (curr_route, n_busses) = bfs_routes_queue.popleft()
            if curr_route in destiny_routes:
                print(f"curr route:{curr_route} is equal to one of destiny routes")
                return n_busses
            for next_route in route_connection_graph[curr_route]:
                if next_route not in seen_routes:
                    bfs_routes_queue.append((next_route, n_busses+1))
                    seen_routes.add(next_route)

        return -1
if __name__ == "__main__":
    sol = Solution()
    distance = sol.numBusesToDestination(routes=[[1,2,7],[3,6,7]], source=1, target=6)
    print(f"distance to destiny is {distance}")
    distance = sol.numBusesToDestination(routes=[[7,12],[4,5,15],[6],[15,19],[9,12,13]], source=15, target=12)
    print(f"distance to destiny is {distance}")