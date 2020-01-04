class Solution(object):
    def distributeCandies(self, candies):
        candydict = {}
        numcandies = len(candies)
        for candy in candies:
            if candy in candydict:
                candydict[candy] += 1
            else:
                candydict[candy] = 1
        types = len(candydict)
        extras = numcandies - types
        if types <= extras:
            return types
        else:
            return types - (types-extras)/2
