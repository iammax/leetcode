class Solution(object):
    def maxProduct(self, words):
        best = 0
        counter1 = 0
        dim = len(words)
        while counter1 < dim-1:
            word1 = words[counter1]
            counter2 = counter1 + 1
            while counter2 < dim:
                word2 = words[counter2]
                if not do_overlap(word1, word2):
                    prod = len(word1)*len(word2)
                    if prod > best:
                        best = prod
                counter2 += 1
            counter1 += 1
        return best
        
def do_overlap(a, b):
    for char in a:
        if char in b:
            return True
    return False
