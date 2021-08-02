class Solution(object):
    def diagonalSum(self, mat):
        dim = len(mat[0])
        total = 0
        for i in range (dim):
            total += mat[i][i]
            total += mat[i][dim-i-1]
        if dim%2 == 1:
            total -= mat[dim/2][dim/2]
        return total
