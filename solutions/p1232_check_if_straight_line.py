class Solution(object):
    def checkStraightLine(self, coordinates):
        numpoints = len(coordinates)
        prevx = coordinates[1][0]
        prevy = coordinates[1][1]
        prevdx = prevx - coordinates[0][0]
        prevdy = prevy - coordinates[0][1]
        try: 
            prevslope = prevdy/prevdx
        except:
            return False
        for q in range (2, numpoints):
            x = coordinates[q][0]
            y = coordinates[q][1]
            dx = x - prevx
            dy = y - prevy
            try:
                slope = dy/dx
            except:
                return False
            print x, y, dx, dy, prevdx, prevdy
            if slope != prevslope:
                return False
            prevslope = slope
            prevx = x
            prevy = y
            prevdx = dx
            prevdy = dy
        return True
