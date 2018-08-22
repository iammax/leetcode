class Solution(object):
    def backspaceCompare(self, S, T):
        news = ''
        newt = ''
        for q in S:
            if q == '#':
                news = news[:-1]
            else:
                news += q
        for q in T:
            if q == '#':
                newt = newt[:-1]
            else:
                newt += q
        return newt == news
