from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        idea1: using a modified search, where the only
        courses added to the heap/queue (whatever DS it may be)
        are the ones where their prereq is already 0.

        Before starting the search, a graph will be created,
        showing (prereq, course). Along with this graph, a vector
        of how many prereqs each course has will be initialized.

        When doing our search, for each edge that touches course C,
        prereq_count[C] -= 1. If prereq_count[C] == 0 then C will
        go into the queue.
        '''
        #initialization
        prereq_count = [0]*numCourses
        prereq_graph = defaultdict(list)
        for i in range(len(prerequisites)):
            course = prerequisites[i][0]
            prereq = prerequisites[i][1]
            prereq_graph[prereq].append(course)
            prereq_count[course] += 1

        order_of_courses = []
        courses_to_take = 0
        for i in range(numCourses):
            if prereq_count[i] == 0:
                order_of_courses.append(i)
                courses_to_take += 1
        
        i = 0
        while i<courses_to_take:
            curr_course = order_of_courses[i]
            #now we have to unlock all prereqs it liberated
            for j in prereq_graph[curr_course]:
                prereq_count[j] -= 1
                if prereq_count[j] == 0:
                    order_of_courses.append(j)
                    courses_to_take += 1
            i += 1
        
        if max(prereq_count) != 0:
            return []
        return order_of_courses

        
if __name__ == "__main__":
    s = Solution()
    print(s.findOrder(numCourses = 2, prerequisites = [[1,0]]))
    print(s.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))