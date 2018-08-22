class Solution(object):
    def projectionArea(self, grid):
        bigtotal = 0
        itotal = 0
        xy = 0
        dim = len(grid)
        bestcols = []
        for i in range (dim):
            imax = 0 
            for j in range (dim):
                Gij = grid[i][j]
                if Gij > imax:
                    imax = Gij
                if Gij > 0:
                    bigtotal += 1
                if i == 0:
                    bestcols.append(Gij)
                else:
                    if Gij > bestcols[j]:
                        bestcols[j] = Gij
            bigtotal += imax
        bigtotal  += sum(bestcols)
        return bigtotal
