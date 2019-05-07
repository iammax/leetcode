class Solution(object):
    def hammingDistance(self, x, y):
        counter = 0
        bigger = max(x,y)
        smaller = min(x,y)
        bin1 = bin(bigger)[2:]
        bin2 = bin(smaller)[2:]
        ham = 0
        print bin1, bin2
        while len(bin2) < len(bin1):
            bin2 = '0' + bin2
        dim = len(bin2)
        while counter < dim:
            if bin1[counter] != bin2[counter]:
                ham += 1
            counter += 1
        return ham
