class Solution(object):
    def makeGood(self, s):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        length = len(s)
        counter = 0
        while counter < length-1:
            if len(s) == 1:
                return s
            if counter < 0:
                counter = 0
            first = s[counter]
            second = s[counter+1]
            print s, counter, first, second
            if first in caps and second in letters:
                if caps.index(first) == letters.index(second):
                    s = s[:counter] + s[counter+2:]
                    length -= 2
                    counter -= 1
                else:
                    counter += 1
            elif first in letters and second in caps:
                if caps.index(second) == letters.index(first):
                    s = s[:counter] + s[counter+2:]
                    length -= 2
                    counter -= 1
                else:
                    counter += 1
            else:
                counter += 1
        return s
