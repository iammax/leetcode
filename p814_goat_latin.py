class Solution(object):
    def toGoatLatin(self, S):
        vowels = ['a', "A", 'e', "E", 'i', 'I', 'o', 'O', 'u', 'U']
        counter = 0
        output = ''
        sentence = S.split()
        dim = len(sentence)
#        print 'sentence: ', sentence
        while counter < dim:
            newword = ''
            thisword = sentence[counter].strip()
#            print thisword, thisword[0]
            firstletter = thisword[0]
            if firstletter in vowels:
                thisword += "ma"
            else:
                thisword = thisword[1:] + '{0}ma'.format(firstletter)
            counter += 1
            for q in range (0, counter):
                thisword += 'a'
            output += '{0} '.format(thisword)
        return output[:-1]
