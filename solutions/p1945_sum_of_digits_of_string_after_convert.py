class Solution:
    
    
    def getLucky(self, s: str, k: int) -> int:
        total = ''
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        power = 0
        for char in s[::-1]:
            num = 1 + alphabet.index(char)
            total = str(num) + total
        total = int(total)
        for q in range (k):
            total = sumdigit(total)
        return total
            

def sumdigit(num: int):
    total = 0
    char = str(num)
    for subchar in char:
        
        total += int(subchar)
    return total
        

