def Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone_dict = {
                "2": ["a", "b", "c"],
                "3": ["d", "e", "g"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"],
        }


