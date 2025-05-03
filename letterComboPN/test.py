from solution import *

answers = [
        [ "23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]],
        [ "", []],
        [ "2", [ "a", "b", "c", "d"]],
        ]



for i in range(len(answers)):
    answer = answers[i]
    print(f"Case {i}")
    print("Solution:")
    print(answer[1])
    print(Solution().letterCombinations(answer[0]))
    print("----------------")
    print()


