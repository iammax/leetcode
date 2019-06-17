class Solution(object):
    def duplicateZeros(self, arr):
        counter = 0
        dim = len(arr)
        while counter < dim:
            here = arr[counter]
            if here == 0:
                subcounter = dim-1
                while subcounter > counter:
                    arr[subcounter] = arr[subcounter-1]
                    subcounter -= 1
                counter +=1
            counter += 1
                
