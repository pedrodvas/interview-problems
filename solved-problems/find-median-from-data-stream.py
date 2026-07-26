import heapq

class MedianFinder:
    def __init__(self):
        self.smallers = [] #max heap
        self.median = None
        self.biggers = [] #min heap

    def addNum(self, num: int) -> None:
        #if bigger than median, add to biggers
        #else, add to smallers
        #We need to rebalance our heaps
        #move elements from the bigger heap
        #into the smaller one
        #when moving these elements, we also always
        # check if our median has to be switched from
        #each of the heaps
        # at the end, we check if it's even or odd. If even
        # we move our median to the proper heap (the one with
        #less elements)
        print("========addNum call start==============")
        if self.median == None:
            self.median = num
            print(f"initialized structure with median {self.median}")
            return
        
        #we already have elements
        if num < self.median:
            #add to smallers heap
            heapq.heappush(self.smallers, -num)
        
        else:
            #add to biggers heap
            heapq.heappush(self.biggers, num)
    '''
        print(f"printing median finder data structure\n"
              f"smallers is\n{self.smallers}\n"
              f"median is {self.median} (can be outdated)\n"
              f"biggers is \n{self.biggers}")
    '''
    def findMedian(self) -> float:
        #each heap will be balanced here, more optimized than balancing it
        #with every addition
        print("=======find median call start=============")
        while len(self.smallers) > len(self.biggers):
            switched_element = heapq.heappop(self.smallers)
            heapq.heappush(self.biggers, -switched_element)
            if self.biggers[0] < self.median:
                '''print(f"switching smallest bigger with median\n"
                      f"median={self.median} bigger[0]:{self.biggers[0]}")'''
                self.median, self.biggers[0] = self.biggers[0], self.median
        while len(self.biggers) > len(self.smallers):
            switched_element = heapq.heappop(self.biggers)
            heapq.heappush(self.smallers, -switched_element)
            if -self.smallers[0] > self.median:
                '''print(f"switching biggest smaller with median\n"
                      f"median={self.median} smaller[0]:{-self.smallers[0]}")'''
                self.median, self.smallers[0] = -self.smallers[0], -self.median

        '''
        print("========\n"
                      f"printing median finder data structure\n"
                      f"smallers is\n{self.smallers}\n"
                      f"median is {self.median} (can be outdated)\n"
                      f"biggers is \n{self.biggers}")
        '''
        if len(self.smallers) > len(self.biggers):
            return -self.smallers[0]/2 + self.median/2
        elif len(self.smallers) < len(self.biggers):
            return self.biggers[0]/2 + self.median/2
        else:
            return self.median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

if __name__ == "__main__":
    obj = MedianFinder()
    for i in [1,2,3]:
        obj.addNum(i)
        median = obj.findMedian()
        print(f"median is {median}")