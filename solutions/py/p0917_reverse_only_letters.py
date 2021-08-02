class Solution(object):
    def reverseOnlyLetters(self, S):
        dim = len(S)
        out = ''
        counter = 0
        rightcounter = dim-1
        caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lowers = 'abcdefghijklmnopqrstuvwxyz'
        while counter < dim:
            thisone = S[counter]
            if thisone in caps or thisone in lowers:
                dummy = False
                while dummy == False:
                    rightone = S[rightcounter]
                    if rightone in caps or rightone in lowers:
                        dummy = True
                        rightcounter -= 1
                    else:
                        rightcounter -= 1
                print 'thisone, rightone: ', thisone, rightone
                out += rightone
            else:
                out += thisone
            counter += 1
        return out
