class Solution(object):
    def matrixReshape(self, nums, r, c):
        ydim = len(nums)
        xdim = len(nums[0])
        total = ydim * xdim
        if total != r*c:
            return nums
        out = []
        thisrow = []
        for y in range (ydim):
            for x in range (xdim):
                thisrow.append(nums[y][x])
                if len(thisrow) == c:
                    out.append(thisrow)
                    thisrow = []
        return out
