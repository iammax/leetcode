class Solution(object):
    def kClosest(self, points, K):
        closest = []
        closepoints = []
        for point in points[0:K]:
            closest.append(point[0]**2 + point[1]**2)
            closepoints.append(point)
        farthest = max(closest)
        for point in points[K:]:
            dist = point[0]**2 + point[1]**2
            if dist < farthest:
                location = closest.index(farthest)
                closest[location] = dist
                farthest = max(closest)
                closepoints[location] = point
        return closepoints
