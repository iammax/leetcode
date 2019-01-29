class Solution(object):
    def strWithout3a3b(self, A, B):
        out = ''
        while A > B and B > 0:
            out += 'aab'
            A -= 2
            B -= 1
        while B > A and A > 0:
            out += 'bba'
            B -= 2
            A -= 1
        while A > 0 and B > 0:
            out += 'ab'
            A -= 1
            B -= 1
        while A > 0:
            out += 'a'
            A -= 1
        while B > 0:
            out += 'b'
            B -= 1
        return out
