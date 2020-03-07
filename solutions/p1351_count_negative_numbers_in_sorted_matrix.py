class Solution(object):
    def countNegatives(self, grid):
        total = 0
        dimy = len(grid)
        dimx = len(grid[0])
        for y in range (dimy-1, -1, -1):
            for x in range(dimx-1, -1, -1):
                here = grid[y][x]
                if here < 0:
                    total += 1
                else:
                    x -1
        return total
