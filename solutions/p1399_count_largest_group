class Solution(object):
    def countLargestGroup(self, n):
        groups = {}
        for num in range (1, n+1):
            strnum = str(num)
            total = 0
            for char in strnum:
                total += int(char)
            if total in groups:
                groups[total].append(num)
            else:
                groups[total] = [num]
        biggest = 0
        num_biggest = 0
        for key in groups:
            num_in_group = len(groups[key])
            if num_in_group > biggest:
                biggest = num_in_group
                num_biggest = 1
            elif num_in_group == biggest:
                num_biggest += 1
        return num_biggest
