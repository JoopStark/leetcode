from solution import *

answers = [
        [ "23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]],
        [ "", []],
        [ "2", [ "a", "b", "c", "d"]],
        ]



for answer in answers:
    print(f"Case {i}")
    print("Solution:")
    print(answer[1])
    print(Solution().threeSum(answer[0]))
    print("----------------")
    print()


