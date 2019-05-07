class Solution(object):
    def transpose(self, A):
        dim_x = len(A)
        dim_y = len(A[0])
        new_matrix = []
        for i in range (0, dim_y):
            newline = []
            for j in range (0, dim_x):
                newline.append(A[j][i])
            new_matrix.append(newline)
        return new_matrix
