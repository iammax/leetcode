class Solution(object):
    def countCharacters(self, words, chars):
        total = 0
        for word in words:
            works = 1
            for letter in word:
                if word.count(letter) > chars.count(letter):
                    works = 0
                    break
            if works:
                total += len(word)
        return total
