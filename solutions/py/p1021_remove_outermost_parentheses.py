class Solution(object):
    def removeOuterParentheses(self, S):
        words = []
        dim = len(S)
        counter = 0
        outword = ''
        left = 0
        right = 0
        while counter < dim:
            thisletter = S[counter]
            outword += thisletter
            if thisletter == '(':
                left += 1
            else:
                right += 1
            if left == right:
                words.append(outword)
                outword = ''
                left = 0
                right = 0
            counter += 1
        out = ''
        for q in words:
            out += q[1:-1]
        return out
