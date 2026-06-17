class Solution:
    '''
    idea: create two dicts, one with starts and
    one with endings of each list. For evenry new
    element, we:
    - check if its start is in the endings
    dict. If it is we merge as other+current
    - check if its ending is in the starts dict.
    If it is we merge as current+other
    won't work because this does not detect one array
    starting at the middle of another
    '''
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        intervals.sort()

        i = 0
        return_list = []
        while i < len(intervals):
            interval = intervals[i]
            while i+1<len(intervals) and interval[1] >= intervals[i+1][0]:
                if intervals[i+1][1] > interval[1]:
                    interval[1] = intervals[i+1][1]
                i +=1
            i += 1
            return_list.append(interval)
        return return_list
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,4], [2,3]]))