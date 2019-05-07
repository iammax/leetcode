class Solution(object):
    def isIsomorphic(self, s, t):
        news = ''
        stdict = {}
        dim = len(s)
        counter = 0
        while counter < dim:
            sc = s[counter]
            tc = t[counter]
            if sc not in stdict:
                if tc in stdict.values():
                    return False
                stdict[sc] = tc
            else:
                if stdict[sc] == tc:
                    pass
                else:
                    return False
            counter += 1
        return True
