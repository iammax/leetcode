class Solution:
    def sortSentence(self, s: str) -> str:
        splitted = s.split()
        out = [0]*len(splitted)
        for word in splitted:
            #print(word, word[-1], word[:-1])
            out[int(word[-1])-1] = word[:-1]
        return ' '.join(out)
