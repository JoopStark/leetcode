class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone_dict = {
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz",
        }

        result = [""]

        for digit in digits:
            combinations = []
            for combination in result:
                for letter in phone_dict[digit]:
                    combinations.append(combination + letter)
            result = combinations

        return result
