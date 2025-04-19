from solution import *

answers = [
    [Solution().isMatch("aa", "a"), False],
    [Solution().isMatch("aa", "a*", True],
    [Solution().isMatch("ab", ".*", True],

     ]

for i in range(len(answers)):
    print(f"Case {i}")
    print("Solution:")
    print(answer[i][0])
    print(answer[i][1])
    print("----------------")
    print()

