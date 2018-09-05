class Solution(object):
    def searchMatrix(self, matrix, target):
        for row in matrix:
            if finder(row, target):
                return True
        return False

def finder(row, target):
    dim = len(row)
    leftbound = 0
    rightbound = dim
    lastone = -1
    while leftbound < rightbound:
        here = (rightbound + leftbound)/2
        if here == lastone:
            return False
        num = row[here]
        if num == target:
            return True
        elif num < target:
            leftbound = here
        else:
            rightbound = here
        lastone = here
    return False
