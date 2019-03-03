class Solution(object):
    def commonChars(self, A):
        chars = {}
        first = A[0]
        for char in first:
            if char not in chars:
                chars[char] = first.count(char)
        for char in chars:
            for word in A:
                chars[char] = min(chars[char], word.count(char))
        out = []
        for char in chars:
            for count in range (chars[char]):
                out.append(char)
        return out
