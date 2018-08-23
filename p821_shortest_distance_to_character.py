class Solution(object):
    def shortestToChar(self, S, C):
        positions = []
        dim = len(S)
        counter = 0
        while counter < dim:
            if S[counter] == C:
                positions.append(counter)
            counter += 1
        outlist = []
        for q in range (0, dim):
            if q in positions:
                outlist.append(0)
            else:
                counter = 0
                found = False
                while found == False:
                    if q + counter in positions:
                        outlist.append(counter)
                        found = True
                    elif q - counter in positions:
                        outlist.append(counter)
                        found = True
                    counter += 1
        return outlist
