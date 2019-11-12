class Solution(object):
    def oddCells(self, n, m, indices):
        mat = [[0 for x in range(m)] for y in range(n)]
        for index in indices:
            r1, c1 = index
            for q in range(m):
                mat[r1][q] = (mat[r1][q]%2)+1
            for q in range (n):
                mat[q][c1] = (mat[q][c1]%2)+1
        tally = 0
        for row in range(n):
            tally += mat[row].count(1)
        return tally
            
