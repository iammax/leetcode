class Solution(object):
    def addStrings(self, num1, num2):
        numdict = {'0':0, '1':1, '2':2, '3':3, '4':4,'5':5,'6':6,'7':7, '8':8,'9':9}
        first = 0
        dim1 = len(num1)
        counter = 0
        while counter < dim1:
            first += numdict[num1[::-1][counter]]*10**counter
            counter += 1
        print 'first num: ', first
        dim2 = len(num2)
        counter = 0
        second = 0
        while counter < dim2:
            second += numdict[num2[::-1][counter]]*10**counter
            counter += 1
        return str(first + second)
