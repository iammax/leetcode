import math

class Solution(object):
    def findNumbers(self, nums):
        total = 0
        for num in nums:
            digs = int(math.log10(num))
            if digs%2 == 1:
                total += 1
        return total
            
