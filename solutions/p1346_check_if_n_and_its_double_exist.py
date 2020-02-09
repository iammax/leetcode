class Solution(object):
    def checkIfExist(self, arr):
        for q in arr:
            if 2*q in arr:
                if q == 0:
                    if arr.count(0) > 1:
                        return True
                else:
                    return True
        return False
