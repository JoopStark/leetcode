# Seven different symbols represent Roman numerals with the following values:
# Symbol	Value

# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000

class Solution():
    def intToRoman(self, s: int) -> str:
        int_dict = {
                1: "I",
                2: "II",
                3: "III",
                4: "IV",
                5: "V",
                6: "VI",
                7: "VII",
                8: "VIII",
                9: "IX",
                10: "X",
                20: "XX",
                30: "XXX",
                40: "XL",
                50: "L",
                60: "LX",
                70: "LXX",
                80: "LXXX",
                90: "XC",
                100: "C",
                200: "CC",
                300: "CCC",
                400: "CD", 
                500: "D",
                600: "DC",
                700: "DCC",
                800: "DCCC",
                900: "CM",
                1000: "M",
                2000: "MM",
                3000: "MMM",
        }

        result = ""

        if s // 1000 >= 1:
            temp = (s//1000) * 1000
            result += int_dict[temp]
            s-= temp
        if s // 100 >= 1:
            temp = (s//100) * 100
            result += int_dict[temp]
            s-= temp
        if s // 10 >= 1:
            temp = (s//10) * 10
            result += int_dict[temp]
            s-= temp
        if s // 1 >= 1:
            result +=  int_dict[(s//1)]
        
        return result
