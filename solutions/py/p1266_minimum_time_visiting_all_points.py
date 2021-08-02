class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        total = 0
        numpoints = len(points)
        index = 1
        prevx = points[0][0]
        prevy = points[0][1]
        while index < numpoints:
            x = points[index][0]
            y = points[index][1]
            total += max(abs(x-prevx), abs(y-prevy))
            prevx = x
            prevy = y
            index += 1
        return total
