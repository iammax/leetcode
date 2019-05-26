class Solution(object):
    def heightChecker(self, heights):
        sort = sorted(heights)
        wrong = 0
        counter = 0
        dim = len(heights)
        while counter < dim:
            a = heights[counter]
            b = sort[counter]
            wrong += (a != b)
            counter += 1
        return wrong
