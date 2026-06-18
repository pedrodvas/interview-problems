from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        '''
        idea is to use a search alongside a 3 coloring to check
        for cycles in a DAG.
        color1 - node not visited
        color2 - visited but not searched completely
        color3 - visited and searched completely
        why would this work to find cycles?
        
        if color1  is reached -> no problem because it still doesn't
        even have children, so it was not its children that reached 
        it
        if color2 is reached-> a chain of sucessors went back
        to the initial node.
        if color 3 is reached-> no problem, because all its sucessors
        were already explored, so the chain did not originate there
        '''
        #initialization
        graph = defaultdict(list)
        for i in prerequisites:
            graph[i[1]].append(i[0])
        
        clean = "clean"
        unfinished = "unfinished"
        finished = "finished"
        vertex_states = [clean]*numCourses
        
        # processing
        for i in range(len(vertex_states)):
            if vertex_states[i] == clean:
                dfs_stack = [(i, unfinished)]
                while dfs_stack:
                    origin_state = dfs_stack.pop()
                    print(f"processing {origin_state}")
                    origin = origin_state[0]
                    edges = graph[origin]
                    if origin_state == finished:
                        vertex_states[origin] = finished
                    if vertex_states[origin] == finished:
                        continue
                    vertex_states[origin] = origin_state[1]
                    dfs_stack.append((origin, finished))
                    
                    for destination_node in edges:
                        #it can be clean, unfinished or finished
                        if vertex_states[destination_node] == clean:
                            # add to stack
                            dfs_stack.append((destination_node, unfinished))
                        elif vertex_states[destination_node] == unfinished:
                            # return False, cycle detected
                            return False
                        elif vertex_states[destination_node] == finished:
                            do_nothing = True
                        else:
                            raise AttributeError
                print(f"finished first connected part")
        print(f"final nu")
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, prerequisites=[[0,1]]))