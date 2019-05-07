class Solution(object):
    def isPowerOfThree(self, n):
        if n == 0:
            return False
        if n == 1:
            return True
        else:
            while n > 3:
            
                n /= 3.
            
            return n == 3.
