from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.times_graph = defaultdict(list)
        self.repetitions_graph = defaultdict(list)
        self.customers = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        departure_place = self.customers[id][0]
        departure_time = self.customers[id][1]

        path = (departure_place, stationName)
        total_time = t-departure_time

        if self.times_graph[path]:
            self.times_graph[path] += total_time
            self.repetitions_graph[path] += 1
        else:
            self.times_graph[path] = total_time
            self.repetitions_graph[path] = 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return (self.times_graph[(startStation, endStation)] / self.repetitions_graph[(startStation,endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)