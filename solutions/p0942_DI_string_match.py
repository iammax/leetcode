class Solution(object):
    def diStringMatch(self, S):
        min = 0
        max = len(S)
        out = []
        for instruction in S:
            
            if instruction == 'I':
                out.append(min)
                min += 1
            else:
                out.append(max)
                max-= 1
        out.append(min)
        return out
