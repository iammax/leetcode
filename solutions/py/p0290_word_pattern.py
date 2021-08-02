class Solution(object):
    def wordPattern(self, pattern, str):
        bij = {}
        dim = len(pattern)
        counter = 0
        splitted = str.split()
        if len(splitted) != dim:
            return False
        while counter < dim:
            word = splitted[counter]
            key = pattern[counter]
            try:
                if bij[key] != word:
                    return False
            except:
                if word in bij.values():
                    return False
                bij[key] = word
            counter += 1
        return True
