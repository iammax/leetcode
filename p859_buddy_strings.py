class Solution(object):
    def buddyStrings(self, A, B):
        dim = len(A)
        if len(A) == 0 and len(B) == 0:
            return False
        if A == B:
            A = sorted(A)
            counter = 0
            while counter < dim-1:
                if A[counter] == A[counter+1]:
                    return True
                else:
                    counter += 1
                return False
        if len(A) != len(B):
            return False
        diffa = []
        diffb = []
        numdiff = 0
        counter = 0
        while counter < dim:
            thisA = A[counter]
            thisB = B[counter]
            if thisA != thisB:
                numdiff += 1
                diffa.append(thisA)
                diffb.append(thisB)
            if numdiff > 2:
                return False
            counter += 1
        if numdiff == 1:
                return False
        diffa = sorted(diffa)
        diffb = sorted(diffb)
        if diffa != diffb:
            return False
        else:
            return True
