class Solution(object):
    def reorderSpaces(self, text):
        if text.count(' ') == 0:
            return text
        spaces = 0
        words = []
        word = ''
        for char in text:
            if char == ' ':
                spaces += 1
                if word != '':
                    words = words + [word]
                    word = ''
            else:
                word = word + char
        if word != '':
            words = words + [word]
        numgaps = len(words) -1
        if numgaps == 0:
            return words[0] + ' '*spaces
        lengap = spaces/numgaps
        extra = spaces%numgaps
        out = ''
        for word in words[:-1]:
            out += word + ' '*lengap
        out += words[-1] + ' '*extra
        return out
        
