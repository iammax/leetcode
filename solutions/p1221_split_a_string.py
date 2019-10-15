class Solution(object):
    def balancedStringSplit(self, s):
        total = 0
        L = 0
        R = 0
        for letter in s:
            if letter == 'R':
                R += 1
            else:
                L += 1
            if L == R and L > 0:
                total += 1
                L = 0 
                R = 0
        return total
