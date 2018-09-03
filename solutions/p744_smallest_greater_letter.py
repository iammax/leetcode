class Solution(object):
    def nextGreatestLetter(self, letters, target):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        index = alphabet.index(target)
        used = {}
        for letter in alphabet:
            used[letter] = 0
        for letter in letters:
            used[letter] += 1
        for q in range (index+1, 26):
            thisletter = alphabet[q]
            if used[thisletter] > 0:
                return thisletter
        for q in range (0, index+1):
            thisletter = alphabet[q]
            if used[thisletter] > 0:
                return thisletter
