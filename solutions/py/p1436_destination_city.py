class Solution(object):
    def destCity(self, paths):
        origins = []
        destinations = []
        for path in paths:
            origins.append(path[0])
            destinations.append(path[1])
        for destination in destinations:
            if destination not in origins:
                return destination
