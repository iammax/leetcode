class Solution(object):
    def countBits(self, num):
        out = []
        for q in range (0, num+1):
            out.append(bin(q).count('1'))
        return out
