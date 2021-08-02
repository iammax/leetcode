class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        if destination < start:
            start, destination = destination, start
        return min(sum(distance[start:destination]),  sum(distance[destination:]) + sum(distance[:start]))
