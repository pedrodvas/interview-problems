import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
        idea1 (bad): try all combinations

        idea2: use dynamic programming to solve
        inductively, comparing solutions
        with job n vs without job n, and then pass
        that

        idea3 (wrong): go through each item, remove all
        the items that block it, add it, then check if 
        it is higher or lower. Won't work because you may need
        to combine two or more jobs to substitute one that is big

        insight: a task doesn't need to worry about completed
        past tasks -> this insight could have led you into the solution.
        After this you could've thought about integrating the current task
        with the highest profit compatible sequence of tasks
        note: I NEED to start by picking one of all the tasks

        '''
        dp_profits = [0]
        dp_ends = [0]
        jobs = sorted(zip(startTime, endTime, profit), key= lambda x: x[1])
        for i in range(len(jobs)):
            start_time = jobs[i][0]
            end_time = jobs[i][1]
            single_profit = jobs[i][2]

            
            last_matchable_task = bisect.bisect_right(dp_ends, start_time)-1
            '''last_matchable_task = 0
            while len(dp_ends) > last_matchable_task and dp_ends[last_matchable_task] <= start_time:
                last_matchable_task += 1
            last_matchable_task -=1'''
            last_matchable_profit = dp_profits[last_matchable_task]
            current_profit = last_matchable_profit+single_profit


            if current_profit > dp_profits[-1]:
                dp_profits.append(current_profit)
            else:
                dp_profits.append(dp_profits[-1])
            dp_ends.append(end_time)
        
        return max(dp_profits)


if __name__ == "__main__":
    sol = Solution()
    print(sol.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]))
    print(sol.jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]))
    print(sol.jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]))
