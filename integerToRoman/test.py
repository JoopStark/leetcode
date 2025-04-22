from solution import *

answers = [
        [3749, "MMMDCCXLIX"],
        [58, "LVIII"],
        [1994, "MCMXCIV"]
        ]



for i in range(len(answers)):
    print(f"Case {i}")
    print("Solution:")
    print(Solution().intToRoman(answers[i][0]))
    print(answers[i][1])
    print("----------------")
    print()


