class Solution(object):
    def isAlienSorted(self, words, order):
        dim = len(words)
        counter = 1
        while counter < dim:
            prev = words[counter-1]
            here = words[counter]
            prev_len = len(prev)
            here_len = len(here)
            letter_counter = 0
            shorter_len = min(prev_len, here_len)
            solved = False
            while letter_counter < shorter_len and solved == False:
                here_letter = here[letter_counter]
                prev_letter = prev[letter_counter]
                if here_letter == prev_letter:
                    pass
                else: 
                    here_location = order.index(here_letter)
                    prev_location = order.index(prev_letter)
                    if here_location < prev_location:
                        return False
                    else:
                        solved = True
                letter_counter += 1
            if not solved:
                if here_len < prev_len:
                    return False
                
            counter += 1
        return True
