class Solution(object):
    def restoreString(self, s, indices):
        out = s
        for index in range (len(s)):
            out = out[:indices[index]] + s[index] + out[indices[index]+1:]
        return out
