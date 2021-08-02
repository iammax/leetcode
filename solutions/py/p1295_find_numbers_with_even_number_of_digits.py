### Method 1: slightly better memory usage, slightly worse runtime, no imports

class Solution(object):
    def findNumbers(self, nums):
        total = 0
        for num in nums:
            st = str(num)
            if len(st)%2 == 0:
                total += 1
        return total


### Method 2: slightly better runtime, using an import, more purely mathematical

#import math

#class Solution(object):
#    def findNumbers(self, nums):
#        total = 0
#        for num in nums:
#            digs = int(math.log10(num))
#            if digs%2 == 1:
#                total += 1
#        return total
#            
