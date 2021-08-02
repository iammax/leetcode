class Solution(object):
    def replaceElements(self, arr):
        biggest = arr[-1]
        dim  = len(arr)
        counter = dim-1
        while counter >= 0:
            here = arr[counter]
            if counter == dim-1:
                arr[counter] = -1
            else:
                arr[counter] = biggest
            if here > biggest:
                biggest = here
            counter -= 1
        arr[-1] = -1
        return arr
