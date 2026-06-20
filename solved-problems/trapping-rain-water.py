class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        idea is use two pointers, one for the maximum
        height for the left, and one that iterates through
        the heights

        for each step, will will add 
        (maximum-curr)
        to the total of water

        but will this work? What if we reach a small wall?
        how do we know how much water is secured?

        One possible solution for this is creating one "bucket"
        for each height. So, if we reach a wall with height = 1
        then we know that every block of water at height = 0 will
        be saved, but using this method will have a use of memory
        O(height)

        according to gemini, the optimal solution can have a use of
        memory equal to O(1), but what could it be?

        AI: the optimal solution would use two pointers, but instead
        of only storing the max and iterating using the other pointer
        like you were thinking, it has one for left max and another for 
        right max.
        Given that we have the current max from left and from right, why
        can we calculate the water as 
        water += max_left - left
        ?
        possible situations:
            unexplored barrier at the middle higher than max_left
            ↓→ if max_right is lower than max_left, than the algorithm
                would add less water than it could as it iterates through 
                the left
                - However, the side with the smaller maximum always is the 
                one to walk
                - In this case, the side with the smaller maximum, is always guaranteed
                to be able to store its water
            '''
        #initialization of vars
        left = 0
        left_max = height[left]
        right = len(height)-1
        right_max = height[right]
        total_water = 0
        while left != right:
            '''
            algorithm
            at each iteration, the place which we point to
            already had its water counted
            '''
            if left_max > right_max:
                right -= 1
                if height[right] > right_max:
                    right_max = height[right]
                    #in this case, no water is added
                else:
                    total_water += right_max - height[right]
            elif left_max <= right_max:
                left += 1
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    total_water += left_max - height[left]
        return total_water

if __name__ == "__main__":
    sol = Solution()
    print(sol.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))