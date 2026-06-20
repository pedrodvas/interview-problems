class Solution:
    def countOrders(self, n: int) -> int:
        '''
        before anythin, my strategy to analyze this problem
        is checking how many different ways two elements can be
        inserted in a list with size 2n, with permutation
        not mattering
        for the first order, we can insert its two parts in an
        empty list, and there is only one way to do that
        n[1] = 1
        for the second, we are searching for ways to put it
        in a list of size 2
        (or here) [pickup 1] (or here) [delivery 1] (or here)
        ↓→ p2 1 => d2 1 2 3
        ↓→ p2 2 => d2 2 3
        ↓→ p2 3 => d2 3
        => sum of different possibilities = 3 + 2 + 1
        (here) [event] (here) [event] (here) [event] (here) [event] (here)
        ↓→p3 1 => d3 5*pos
        ↓→p3 2 => d3 4*pos
        ↓→p3 3 => d3 3*pos
        ↓→p3 4 => d3 2*pos
        ↓→p3 5 => d3 1*pos
        15 different * 6 possibilities from the case before

        how many different positions do we have at order n? 2n -1
        sum from 1 to 2n-1
        sum for 1 to n is n*(n+1)/2
        for 1: 1= 1*2/2 ok
        2: 1+2=3=2*(2+1)/2 ok
        3: 1+2+3 = 6 = 3*(3+1)/2 ok

        substituting (2n-1) -> n
        (2n-1)*(2n-1+1)/2 = (2n-1)*2n/2 = (2n-1)*n
        '''
        initial = 1
        for i in range(1,n+1):
            initial *=(2*i-1)*i
        return initial%(10**9+7)