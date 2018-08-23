class Solution(object):
    def firstBadVersion(self, n):
        leftbound = 0
        rightbound = n
        while True:
            counter = (leftbound + rightbound)/2
            thisone = isBadVersion(counter)
            if thisone:
                if not isBadVersion(counter-1):
                    return counter
                else:
                    rightbound = counter
            else:
                if isBadVersion(counter+1):
                    return counter+1
                else:
                    leftbound = counter
