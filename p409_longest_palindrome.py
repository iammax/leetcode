class Solution(object):
    def longestPalindrome(self, s):
        thedict = {}
        for char in s:
            if char not in thedict:
                thedict[char] = 1
            else:
                thedict[char] += 1
        total = 0
        odd_counter = 0
        numkeys = len(thedict.keys())
        if numkeys == 1:
            return thedict[thedict.keys()[0]]
        else:
            for key in thedict.keys():
                if thedict[key] %2 == 1 and odd_counter == 0:
                    total += thedict[key]
                    odd_counter = 1
                else:
                    total += thedict[key]/2*2
            return total
