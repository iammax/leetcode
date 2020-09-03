class Solution(object):
    def thousandSeparator(self, n):
        out = ''
        counter = 0
        for letter in str(n)[::-1]:
            if counter == 3:
                out = '.' + out
                counter = 0
            out = letter + out
            counter += 1
        return out
