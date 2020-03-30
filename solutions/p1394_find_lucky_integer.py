class Solution(object):
    def findLucky(self, arr):
        succeeded = {}
        for num in arr:
            if num not in succeeded:
                if arr.count(num) == num:
                    succeeded[num] = 1
                else:
                    succeeded[num] = 0
        out = []
        for num in succeeded:
            if succeeded[num] == 1:
                out.append(num)
        if len(out) > 0:
            return max(out)
        else:
            return -1
