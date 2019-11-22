class Solution(object):
    def shiftGrid(self, grid, k):
        #This is definitely not the fastest way to execute the operation, but this is a quick brute force method that is very quick to implement
        rowlen = len(grid[0])
        cols = len(grid)
        newmat = [[0 for i in range(rowlen)] for j in range(cols)]
        newmat[0][0]=1
        for y in range (0, cols):
            newrow = []
            for x in range(0, rowlen):
                val = grid[y][x]
                newx = x + k
                newy = (y + newx/rowlen)%cols
                newx = newx%rowlen
                newmat[newy][newx] = val
        return newmat
