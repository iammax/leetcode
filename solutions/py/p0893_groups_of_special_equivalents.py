class Solution(object):
    def numSpecialEquivGroups(self, A):
        dictionary = {}
        for word in A:
            dim = len(word)
            counter = 0
            evens = []
            odds = []
            while counter < dim:
                if counter % 2 == 0:
                    evens.append(word[counter])
                else:
                    odds.append(word[counter])
                counter += 1
            evens = sorted(evens)
            odds = sorted(odds)
            s = str([evens, odds])
            if s not in dictionary:
                dictionary[s] = [word]
            else:
                dictionary[s].append(word)
        return len(dictionary.values())
