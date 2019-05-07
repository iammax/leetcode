class Solution(object):
    def letterCasePermutation(self, S):
        caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        smalls = 'abcdefghijklmnopqrstuvwxyz'
        outs = ['']
        for char in S:
            done = False
            dim = len(outs)
            if char in caps:
                done = True
                oldouts = outs
                outs = []
                for q in range (0, dim):
                    thisone = oldouts[q]
                    outs.append(thisone + smalls[caps.index(char)])
                    outs.append(thisone + char)
            if char in smalls:
                done = True
                oldouts = outs
                outs = []
                for q in range (0, dim):
                    thisone = oldouts[q]
                    outs.append(thisone + char)
                    outs.append(thisone + caps[smalls.index(char)])
            if not done:
                for q in range(0, dim):
                    outs[q] = outs[q] + char
        return outs
