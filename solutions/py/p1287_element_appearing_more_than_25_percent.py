#assumes array is sorted  
class Solution(object):
    def findSpecialInteger(self, arr):
       dim = len(arr)
        prev = arr[0]
        if dim == 1:
            return prev
        cutoff = int(dim*.25)
        counted = 1
        for entry in arr[1:]:
            if entry == prev:
                counted += 1
                if counted > cutoff:
                    return entry
            else:
                prev = entry
                counted = 1
        
