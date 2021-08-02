class Solution(object):
    def peakIndexInMountainArray(self, A):
        counter = 0
        while A[counter] < A[counter+1]:
            counter +=1
        return counter
