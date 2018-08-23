class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        smalls = 'abcdefghijklmnopqrstuvwxyz'
        words = {}
        for w in paragraph.split():
            word = ''
            for char in w:
                if char in smalls:
                    word += char
                elif char in caps:
                    word += smalls[caps.index(char)]
                else:
                    pass
            if word in banned:
                pass
            else:
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
        best = ''
        bestnum = 0
        for word in words:
            if words[word] > bestnum:
                bestnum = words[word]
                best = word
        return best
