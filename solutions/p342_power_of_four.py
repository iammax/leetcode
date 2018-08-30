class Solution(object):
    def isPowerOfFour(self, num):
        if num < 1:
            return False
        while num > 1:
            if num % 4 != 0:
                return False
            num /= 4
        return True
