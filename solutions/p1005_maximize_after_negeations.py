class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        while K > 0:
            A = sorted(A)
            A[0] = -A[0]
            K -= 1
        return sum(A)
