class Solution(object):
    def bitwiseComplement(self, N):
        forward = bin(N)[2:]
        rev = ''
        for digit in forward:
            if digit == '1':
                rev = '0' + rev
            else:
                rev = '1' + rev
        total = 0
        power = 0
        for digit in rev:
            digit = int(digit)
            total += digit*(2**power)
            power += 1
        return total
