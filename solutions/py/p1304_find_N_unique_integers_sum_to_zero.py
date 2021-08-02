class Solution(object):
    def sumZero(self, n):
        out = [0]*n
        total = 0
        for q in range (0, n-1):
            out[q] = q
            total += q
        out[-1] = -total
        return out
            
