# first row index = 2(numRows - 1)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        string_length = len(s)
        result = ""

        for j in range(0,4):
            letter = j*(numRows + 1)
            result += str(letter) 
        print(result)
            


