class Solution(object):
    def oddCells(self, n, m, indices):
        mat = [[0 for x in range(m)] for y in range(n)]
        for index in indices:
            r1, c1 = index
            for q in range(m):
                mat[r1][q] += 1
            for q in range (n):
                mat[q][c1] += 1
        tally = 0
        for x in range(m):
            for y in range(n):
                digit = mat[y][x]
                if digit%2 == 1:
                    tally += 1
        return tally
            
