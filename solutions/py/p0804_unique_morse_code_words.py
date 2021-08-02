class Solution(object):
    def uniqueMorseRepresentations(self, words):
        alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letters = 'abcdefghijklmnopqrstuvwxyz'
        morse_words = []
        for word in words:
            morse_word = ''
            for letter in word:
                morse_word += alphabet[letters.index(letter)]
            if morse_word not in morse_words:
                morse_words.append(morse_word)
        return len(morse_words)
