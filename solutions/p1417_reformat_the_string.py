class Solution(object):
    def reformat(self, s):
        nums = '0123456789'
        letters = 'abcdefghijklmnopqrstuvwxyz'
        ints = []
        chars = []
        for thing in s:
            if thing in nums:
                ints.append(thing)
            else:
                chars.append(thing)
        if abs(len(ints)-len(chars)) > 1:
            return ''
        else:
            out = ''
            smaller = min(len(ints),len(chars))
            for q in range(smaller):
                out += (ints[q] + chars[q])
            if len(ints) > len(chars):
                out += ints[-1]
            elif len(ints) < len(chars):
                out = chars[-1] + out
            return out
