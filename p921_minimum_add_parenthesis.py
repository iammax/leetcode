class Solution(object):
    def minAddToMakeValid(self, S):
        invalids = 0
        lefts = 0
        rights = 0
        for q in S:
            if q == '(':
                lefts += 1
            else:
                if lefts > 0:
                    lefts -= 1
                else:
                    invalids += 1
        print invalids, lefts, rights
        return invalids + lefts + rights
