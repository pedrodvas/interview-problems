from collections import deque

class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        '''
        we are given a 2d grid of three kinds of values
        -1: wall
        0: gate = destinations
        INF: =2**31-1 = empty room
        '''
        '''
        solution will be using a bfs, where we will
        have a center that connects to the destinations with
        distance 0. 
        After that we will do a bfs normally, adding pairs
        of (location, distance) to the bfs queue as we iterate
        through the list itself
        '''
        INF = 2147483647
        bfs_queue = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    bfs_queue.append((i,j))
        
        print(bfs_queue)
        while bfs_queue:
            curr_node = bfs_queue.popleft()
            i, j = curr_node[0], curr_node[1]
            curr_val = rooms[i][j]
            #look at the neighboors and update 
            #their distances
            if j!=0 and rooms[i][j-1] == INF:
                rooms[i][j-1] = curr_val+1
                bfs_queue.append((i, j-1))
            if i!=0 and rooms[i-1][j] == INF:
                rooms[i-1][j] = curr_val+1
                bfs_queue.append((i-1, j))
            if i<len(rooms)-1 and rooms[i+1][j] == INF:
                rooms[i+1][j] = curr_val+1
                bfs_queue.append((i+1, j))
            if j<len(rooms[i])-1 and rooms[i][j+1] == INF:
                rooms[i][j+1] = curr_val+1
                bfs_queue.append((i, j+1))
        
        return rooms


if __name__ == "__main__":
    sol = Solution()
    INF = 2147483647
    teste_rooms = [
    [0, -1, INF, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, INF],
    [-1, -1, -1, 0]
    ]
    print(sol.wallsAndGates(teste_rooms))