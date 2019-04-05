class Solution(object):
    def prefixesDivBy5(self, A):
        out = []
        number = 0
        for i in range (0, len(A)):
            number *= 2
            number += A[i]
            out.append(number%5 == 0)
        return out
