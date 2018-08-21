class Solution(object):
    def reorderedPowerOf2(self, N):
        pows = []
        for q in range (0, 31):
            pows.append(2**q)
        dim = len(str(N))
        for item in pows:
            if len(str(item)) == dim:
                if sorted(str(item)) == sorted(str(N)):
                    return True
        return False
