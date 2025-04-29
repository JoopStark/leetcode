from solution import *

answers = [
       [[-1, 2, 1, 4], 1, 2],
       [[0, 0, 0], 1, 2],
        ]



for i in range(len(answers)):
    print(f"Case {i}")
    print("Solution:")
    print(answers[i][2])
    print(Solution().threeSumClosest(answers[i][0], answers[i][1]))
    print("----------------")
    print()


