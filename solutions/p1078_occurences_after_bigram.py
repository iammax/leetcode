class Solution(object):
    def findOcurrences(self, text, first, second):
        splitted = text.split()
        counter = 1
        outs = []
        while counter < len(splitted)-1:
            here = splitted[counter]
            if here == second:
                if splitted[counter-1] == first:
                    outs.append(splitted[counter+1])
            counter += 1
        return outs
