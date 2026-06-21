from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        idea1: use max on each iteration
        will result in a o(n²) perf and is trivial

        idea2:use a max heap, but this will lead to a
        o(nlgn) solution, which is still not the best possible
        
        idea3: use a double linked list, where its 0th
        element always points to the biggest number.
        When a new element is inserted into the list,
        it pops the 0th element until it is at leat equal
        to himself
        '''
        biggest = deque([0])
        for i in range(1, k):
            while biggest and nums[biggest[-1]] < nums[i]:
                biggest.pop()
            biggest.append(i)
        
        return_list = [nums[biggest[0]]]
        for i in range(k, len(nums)):
            if i >= biggest[0]+k:
                biggest.popleft()
            while biggest and nums[biggest[-1]] < nums[i]:
                biggest.pop()
            biggest.append(i)
            return_list.append(nums[biggest[0]])
        
        return return_list


if __name__ == "__main__":
    sol = Solution()
    a = sol.maxSlidingWindow([1,3,1,2,0,5], 3)
    print(a)