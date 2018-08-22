class Solution(object):
    def intToRoman(self, num):
        total = ''
        while num >= 1000:
            total += "M"
            num -= 1000
        if 899 < num <= 999:
            total += "CM"
            num -= 900
        if 500 <= num < 900:
            total += "D"
            num -= 500
        if 399 < num <= 499:
            total += "CD"
            num -= 400
        while num > 99:
            total += "C"
            num -= 100
        if 89 < num <= 99:
            total += "XC"
            num -= 90
        if 50 <= num < 90:
            total += "L"
            num -= 50
        if 39 < num <= 49:
            total += "XL"
            num -= 40
        while num > 9:
            total += "X"
            num -= 10
        if num == 9:
            total += "IX"
            num = 0
        if 5 <= num < 9:
            total += "V"
            num -= 5
        if num == 4:
            total += "IV"
            num = 0
        while num > 0:
            total += "I"
            num -= 1
        return total
