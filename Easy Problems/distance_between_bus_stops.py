class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        total = sum(distance)
        clock = sum(distance[start:destination])
        counter = total - clock
        return min(clock, counter)
