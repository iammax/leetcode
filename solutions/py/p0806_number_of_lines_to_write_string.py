class Solution(object):
    def numberOfLines(self, widths, S):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        w_dict = {}
        for counter in range (0, 26):
            w_dict[alphabet[counter]] = widths[counter]
        width = 0
        lines = 1
        for letter in S:
            this_width = w_dict[letter]
            width += this_width
            if width == 100:
                lines += 1
                width = 0
            elif width >= 100:
                lines += 1
                width = this_width
        return [lines, width]
