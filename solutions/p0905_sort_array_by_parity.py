class Solution(object):
    def sortArrayByParity(self, A):
        out = []
        for num in A:
            if num%2 == 1:
                out.append(num)
            else:
                out = [num] + out
        return out
