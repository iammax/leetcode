class Solution(object):
    def convertToBase7(self, num):
        ab = abs(num)
        out = ''
        if num == 7:
            return '10'
        if num == -7:
            return '-10'
        if abs(num) < 7:
            return str(num)
        while ab > 1:
            out += str(ab% 7)
            ab /=7
        if ab == 1:
            out += '1'
        if num >= 0:
            return out[::-1]
        else:
            return '-'+ out[::-1] 
