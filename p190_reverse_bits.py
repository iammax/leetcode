class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        orig = bin(n)[2:]
        length = len(orig)
        while length < 32:
            orig = '0' + orig
            length = len(orig)
        rev = orig[::-1]
        newval = int(rev, 2)
        return newval
