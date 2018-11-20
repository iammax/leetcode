class Solution(object):
    def validMountainArray(self, A):
        peaked = False
        if len(A) < 3:
            return False
        prev = A[0]
        if A[1] < prev:
            return False
        for here in A[1:]:
            if not peaked:
                if here < prev:
                    peaked = True
                elif here == prev:
                    return False
            else:
                if here > prev or here == prev:
                    return False
            prev = here
        return peaked
