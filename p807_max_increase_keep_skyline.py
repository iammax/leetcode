class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        xdim = len(grid[0])
        ydim = len(grid)
        total = 0
        ymaxs = []
        xmaxs = []
        for y in range (ydim):
            ymaxs.append(max(grid[y]))
        for x in range (xdim):
            thiscol = []
            for y in range (0, ydim):
                thiscol.append(grid[y][x])
            xmaxs.append(max(thiscol))
        total = 0
        for y in range (ydim):
            for x in range (xdim):
                total += (min([xmaxs[x], ymaxs[y]]) - grid[x][y])
        return total
