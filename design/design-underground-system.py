from collections import defaultdict
class UndergroundSystem:
    def __init__(self):
        self.avg_time = defaultdict(lambda: (0, 0)) # key: tuple of start and end location, val: avg time, times
        self.current_location = dict() # key: id, val: tuple of current location and time

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.current_location[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_location, start_time = self.current_location[id]
        route = (start_location, stationName)
        current_avg, times = self.avg_time[route]
        self.avg_time[route] = ((current_avg*times + (t - start_time))/(times + 1), times+1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        current_avg, times = self.avg_time[(startStation, endStation)]
        return current_avg

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)