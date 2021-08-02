class Solution(object):
    def maxPower(self, s):
        consec = 1
        best = 0
        prev = s[0]
        if len(s) == 1:
            return 1
        for letter in s[1:]:
            if letter == prev:
                consec += 1
            else:
                if consec > best:
                    best = consec
                consec = 1
            prev = letter
        return max (best, consec)
