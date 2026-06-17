import bisect

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        '''
        testing each weight: O(n²) and dumb, probably
        there is something better
        
        idea2: searching through weights with bin search,
        for each weight we check if it can deliver the packages
        '''
        #initialization
        min_weight = max(weights)
        max_weight = sum(weights)
        possible_weights = list(range(min_weight, max_weight+1))
        '''
        how the bin search will work:
        

        if guess == max or guess == min can we stop processing?
        suppose
        283 = min, guess
        284 = max
        '''
        pos = bisect.bisect_left(range(min_weight, max_weight+1), -days,
                           key=lambda x: self.estimate_time(weights, x))
        
        return min_weight+pos
        


    def estimate_time(self, weights: list[int], capacity):
        current_package = 0
        trips = 0
        current_weight = 0
        while current_package<len(weights):
            if current_weight+weights[current_package]<=capacity:
                current_weight += weights[current_package]
                current_package += 1
            else:
                trips += 1
                current_weight = 0

        trips += 1
        return -trips

if __name__ == "__main__":
    sol = Solution()
    print(sol.estimate_time([1,2,3], 6))
    sol.shipWithinDays([1,2,3], 1)