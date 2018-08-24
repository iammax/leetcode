class Solution(object):
    def flipAndInvertImage(self, A):
        def flip(entry):
            newone = []
            size = len(entry)
            for q in range (0, size):
                index = size - q - 1
                newone.append(entry[index])
            return newone
        def inverse(entry):
            newone = []
            for q in range (0, len(entry)):
                if entry[q] == 0:
                    newone.append(1)
                else:
                    newone.append(0)
            return newone
        entrylist = []
        for q in A:
            entrylist.append( inverse(flip(q)))
        return entrylist
