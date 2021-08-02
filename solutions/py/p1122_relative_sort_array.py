class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        inv = {}
        remainders = {}
        for a in arr1:
            if a in arr2:
                if a in inv:
                    inv[a] += 1
                else:
                    inv[a] = 1
            else:
                if a in remainders:
                    remainders[a] += 1
                else:
                    remainders[a] = 1
        out = []
        for b in arr2:
            if b in inv:
                for q in range (inv[b]):
                    out.append(b)
        for c in sorted(remainders):
            for q in range (remainders[c]):
                out.append(c)
        return out
        
