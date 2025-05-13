from solution import *
import pandas as pd



data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
scores = pd.DataFrame(data, columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})

answers = [
        ["DT", scores],
        ]

for i in range(len(answers)):
    answer = answers[i]
    print(f"Case{i}")
    print("Solution:")
    print(answer[0])
    print(order_scores(answer[1]))
    print("-------------")
    print()

