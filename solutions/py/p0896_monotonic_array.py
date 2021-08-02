class Solution(object):
    def isMonotonic(self, A):
        dim = len(A)
        direction = 0
        counter = 1
        prev = A[0]
        while counter < dim:
            here = A[counter]
            if direction == 0:
                if here > prev:
                    direction = 1
                elif here < prev:
                    direction = -1
            elif direction == 1:
                if here < prev:
                    return False
            else:
                if here > prev:
                    return False
            counter += 1
            prev = here
        return True
