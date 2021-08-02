class Solution(object):
    def searchMatrix(self, matrix, target):
        ydim = len(matrix)
        try:
            xdim = len(matrix[0])
        except:
            xdim = None
        try:
            dim = xdim * ydim
        except:
            dim = ydim
        leftbound = 0
        rightbound = dim-1
        if leftbound == rightbound:
            if matrix[0][0] == target:
                return True
            else:
                return False
        while leftbound <= rightbound:
            index = (leftbound + rightbound)/2
            yindex, xindex = indexer(index, xdim)
            num = matrix[yindex][xindex]
            if num == target:
                return True
            elif num > target:
                rightbound = index
            else:
                leftbound = index
            try:
                if lastindex == index:
                    break
            except:
                pass
            lastindex = index
        try:
            yindex, xindex = indexer(index+1, xdim)
            if matrix[yindex][xindex] == target:
                return True
            else:
                return False
        except:
            return False
        
def indexer(num, xdim): #returns [y index, x index]
    if xdim:
        return [num/xdim, num%xdim]
    else:
        return num
