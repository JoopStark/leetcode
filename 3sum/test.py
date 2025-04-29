from solution import *

answers = [
        [[-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]],
        [[0, 1, 1], []],
        [[0, 0, 0], [[0, 0, 0]]],
        ]



for i in range(len(answers)):
    print(f"Case {i}")
    print("Solution:")
    print(answers[i][1])
    print(Solution().threeSum(answers[i][0]))
    print("----------------")
    print()


