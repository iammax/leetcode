class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        most = max(candies)
        out = []
        for kid in candies:
            if kid + extraCandies >= most:
                out.append(1)
            else:
                out.append(0)
        return out
