class Solution(object):
    def countSubstrings(self, s):
        counter = 0
        dim = len(s)
        for start in range (0, dim+1):
            for end in range (start+1, dim+1):
                sub = s[start:end]
                counter += (sub == sub[::-1])
        return counter
