class Solution(object):
    def checkRecord(self, s):
        if len(s) > 1:
            As = 0
            prevprev = s[0]
            prev = s[1]
            if prevprev == 'A':
                As += 1
            if prev == 'A':
                As += 1
            if As == 2:
                return False
            dim = len(s)
            counter = 2
            while counter < dim:
                thisone = s[counter]
                if thisone == 'A':
                    As += 1
                if As > 1:
                    return False
                if thisone == 'L' and prev == 'L' and prevprev == 'L':
                    return False
                counter += 1
                prevprev = prev
                prev = thisone
            return True
        return True
