class Solution(object):
    def distributeCandies(self, candies):
        
        numcandies = len(candies)
        candyset = set(candies)
        types = len(candyset)
        extras = numcandies - types
        if types <= extras:
            return types
        else:
            return types - (types-extras)/2
