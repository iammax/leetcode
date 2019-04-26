class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        celldict = {}
        for i in range (C):
            for j in range (R):
                dist = abs(i-c0) + abs(j-r0)
                try:
                    celldict[dist].append(j + (i*R))
                except:
                    celldict[dist] = [j + (i*R)]
        out = []
        for cell in celldict:
            points = celldict[cell]
            for point in points:
                out.append([point%R, point/R])
        return out
