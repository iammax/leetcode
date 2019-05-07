class Solution(object):
    def isBoomerang(self, points):
        x1 = float(points[0][0])
        y1 = float(points[0][1])
        x2 = float(points[1][0])
        y2 = float(points[1][1])
        x3 = float(points[2][0])
        y3 = float(points[2][1])
        if not samepoint(x1, x2, y1, y2) and not samepoint(x1, x3, y1, y3) and not samepoint(x2, x3, y2, y3):
            if (y2-y1) == 0:
                return (y3-y1) !=0
            if (y3-y1) == 0:
                return (y2-y1) != 0
            slope1 = (x2-x1)/(y2-y1)
            slope2 = (x3-x1)/(y3-y1)
            return slope1 != slope2

def samepoint(x1, x2, y1, y2):
    return  x1 == x2 and y1 == y2
