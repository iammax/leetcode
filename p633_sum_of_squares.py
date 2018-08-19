class Solution(object):
    def judgeSquareSum(self, c):
        if c == 0:
            return True
        elif c < 0:
            return False
        counter = 1
        target = int(c**.5)
        while counter <= target:
            rem = (c-(counter**2))**.5
            if rem.is_integer():
                return True
            counter += 1
        return False
