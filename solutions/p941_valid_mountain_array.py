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

#Alternate solution; same speed according to leetcode
class Solution(object):
    def validMountainArray(self, A):
        if len(A) < 3:
            return False
        biggest = max(A)
        if A.count(biggest) > 1:
            return False
        peak = A.index(biggest)
        rise = A[:peak]
        fall = A[peak+1:]
        if len(rise) == 0 or len(fall) == 0 or len(rise) != len(set(rise)) or len(fall) != len(set(fall)):
            return False
        return rise == sorted(rise) and fall == sorted(fall)[::-1]
