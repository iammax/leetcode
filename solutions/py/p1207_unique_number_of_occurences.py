class Solution(object):
    def uniqueOccurrences(self, arr):
        vals = []
        freqs = []
        for val in arr:
            if val not in vals:
                freq = arr.count(val)
                if freq not in freqs:
                    vals.append(val)
                    freqs.append(freq)
                else:
                    return 0
        return 1
