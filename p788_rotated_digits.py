class Solution(object):
    def rotatedDigits(self, N):
        valid = 0
        for q in range (0, N+1):
            valid += isgood(q)
        return valid

def isgood(num):
    selfs = [0,1,8]
    goods = [2,5,6,9]
    bad = [3,4,7]
    goodcount = 0
    for char in str(num):
        char = int(char)
        if char in bad:
            return 0
        if char in goods:
            goodcount += 1
    if goodcount > 0:
        return 1
    else:
        return 0
