class Solution(object):
    def sortArrayByParityII(self, A):
        odds = []
        evens = []
        for num in A:
            if num%2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        out = []
        for i in range (0, len(odds)):
            out.append(evens[i])
            out.append(odds[i])
        return out
