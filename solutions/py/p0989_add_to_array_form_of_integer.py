class Solution(object):
    def addToArrayForm(self, A, K):
        def arraytonum(arr):
            total = 0
            dim = len(arr)
            counter = 0
            while counter < dim:
                total += arr[counter]*10**(dim-1-counter)
                counter += 1
            return total
        out = []
        counter = 0
        st = str(K + arraytonum(A))
        for q in st:
            out.append(int(q))
        return out
