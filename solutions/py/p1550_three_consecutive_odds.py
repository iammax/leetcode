class Solution(object):
    def threeConsecutiveOdds(self, arr):
        counter = 0
        oddcount = 0
        while counter < len(arr):
            here = arr[counter]
            if here % 2 == 1:
                oddcount += 1
            else:
                oddcount = 0
            if oddcount == 3:
                return True
            counter += 1
        return False
                
                
