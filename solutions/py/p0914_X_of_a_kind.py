class Solution(object):
    def hasGroupsSizeX(self, deck):
        counts = {}
        for card in deck:
            if card in counts:
                counts[card] += 1
            else:
                counts[card] = 1
        smallest = min(counts.values())
        numvals = len(counts.values())
        for q in range (2, smallest+1):
            dummy = True
            counter = 0
            hits = 0
            while dummy == True and counter < numvals:
                thisval = counts.values()[counter]
                if thisval % q == 0:
                    hits += 1
                else:
                    dummy = False
                counter += 1
            if hits == numvals:
                return True
        return False
