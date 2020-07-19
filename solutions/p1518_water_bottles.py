class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        total = numBottles
        empty = numBottles
        while empty >= numExchange:
            newbottles = empty /numExchange
            total += newbottles
            empty -= newbottles*(numExchange-1)
        return total
