class Solution(object):
    def minAddToMakeValid(self, S):
        if len(S) < 2: return len(S)
        dim = len(S)
        invalid = 0
        counter = 0
        dummy = False
        finished = False
        while dummy == False:
            if len(S) == 1:
                return invalid + 1
            thisleft = S[counter]
            if thisleft == ')':
                invalid += 1
                S = removeindex(S, counter)
            else:
                subcounter = counter+1
                subdummy = False
                while subdummy == False:
                    thisright = S[subcounter]
                    if thisright == ')':
                        S = removeindex(S, subcounter)
                        S = removeindex(S, counter)
                        subdummy = True
                    subcounter += 1 
                    if subcounter == len(S) and thisright == '(':
                        subdummy = True
                        dummy = True
            counter += 0
            if counter == len(S):
                dummy = True
        return len(S) - counter + invalid
def removeindex(S, index):
    return S[:index] + S[1+index:]
