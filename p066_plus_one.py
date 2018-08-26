class Solution(object):
    def plusOne(self, digits):
        pos = len(digits)-1
        done = False
        add = 0
        while done == False:
            thisdigit = digits[pos]
            if thisdigit < 9:
                digits[pos] = thisdigit+1
                done = True
            elif thisdigit == 9 and pos > 0:
                digits[pos] = 0
                add += 1
                pos -= 1
            elif thisdigit == 9 and pos == 0:
                digits[pos] = 0
                digits.insert(0, 1)
                return digits
        return digits
