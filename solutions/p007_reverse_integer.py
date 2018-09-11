class Solution(object):
    def reverse(self, x):
        if x < 0:
            result = int("-{0}".format(str(x)[1:][::-1]))
        else:
            result =  int(str(x)[::-1])
        if abs(result) < 2**31:
            return result
        else:
            return 0
