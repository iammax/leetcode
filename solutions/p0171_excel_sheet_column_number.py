class Solution(object):
    def titleToNumber(self, s):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letterdict = {}
        dim = len(letters)
        counter = 0
        while counter < dim:
            letterdict[letters[counter]] = counter + 1
            counter += 1
        total = 0
        s = s[::-1]
        dim = len(s)
        counter = 0
        while counter < dim:
            thisval = letterdict[s[counter]]
            total += (26**counter)*thisval
            counter += 1
        return total 
