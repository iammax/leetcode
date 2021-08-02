class Solution(object):
    def countServers(self, grid):
        rowlen = len(grid[0])
        numrows = len(grid)
        total = 0
        for y in range (numrows):
            row = grid[y]
            if row.count(1) > 1:
                for x in range (rowlen):
                    if grid[y][x] != 0:
                        grid[y][x] = 2
        for x in range (rowlen):
            col = []
            for y in range (numrows):
                col.append(grid[y][x])
            if col.count(1) + col.count(2) > 1:
                for y in range (numrows):
                    if grid[y][x] != 0:
                        grid[y][x] = 2
        for row in grid:
            total += row.count(2)
        return total
