class Solution(object):
    def findComplement(self, num):
        thing = bin(num)[2:]
        out = ''
        for q in thing:
            if q == '1':
                out += '0'
            else:
                out += '1'
        return int(out, 2)
