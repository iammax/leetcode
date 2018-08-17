class Solution(object):
    def uncommonFromSentences(self, A, B):
        alllist = []
        for q in A.split():
                alllist.append(q)
        for q in B.split():
                alllist.append(q)
        outlist = []
        for q in alllist:
            if alllist.count(q) == 1:
                outlist.append(q)
        return outlist
