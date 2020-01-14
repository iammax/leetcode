class Solution(object):
    def freqAlphabets(self, s):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        encoder = {}
        counter = 1
        for letter in alphabet:
            encoder[str(counter)] = letter
            counter += 1
        print encoder
        counter = 0
        dim = len(s)
        splitted = s.split('#')
        output = ''
        
        if len(splitted[-1]) == 2:
            splitted = splitted[:-1] + [splitted[-1][0]] + [splitted[-1][1]]
        for item in splitted:
            singles = item[:-2]
            final = item[-2:]
            
            for char in singles:
                output += encoder[char]
            if len(final) > 0:
                output += encoder[final]
        return output
