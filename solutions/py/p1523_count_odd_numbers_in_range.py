class Solution(object):
    def countOdds(self, low, high):
        gap = high-low
        if gap%2 == 0 and low%2 == 0:
            return gap/2
        else:
            return 1 + (gap/2)
