class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV",
            1: "I"
        }

        roman = ""
        
        for value, symbol in roman_map.items():
            count = num // value
            num -= count * value
            roman += symbol * count
        return roman

obj = Solution()
print(obj.intToRoman(23456))

# # method 2

#         digits =[(1000, "M"),
#         (900,"CM"),(500,"D"),(400,"CD"), (100, "C"),  
#         (90, "XC"),(50, "L"),(40, "XL"),(10, "X"),
#         (9, "IX"),(5, "V"),(4, "IV"),(1, "I")]

#         roman_digits = []
#         for value, symbol in digits:
#             if num == 0:
#                 break
#             count, num = divmod(num, value)
#             roman_digits.append(symbol*count)

#         return "".join(roman_digits)