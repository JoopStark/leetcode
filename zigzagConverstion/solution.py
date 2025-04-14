# first row index = 2(numRows - 1)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        string_length = len(s)
        result = ""

        for j in range(0,string_length):
            letter_index = j*(numRows + 1)
            if letter_index < string_length:
                result += s[letter_index]
            else:
                break
        # print(result)
       
        for i in range(1, numRows - 1):
            result += s[i]
            for j in range(1, string_length):
                letter_index = i + j*(numRows + 1)
                letter_index_minus = letter_index - (i * 2)
                if letter_index_minus < string_length:
                    result += s[letter_index_minus]
                else:
                    break
                if letter_index < string_length:
                    result += s[letter_index]
                else:
                    break


        for j in range(0, string_length):
            letter_index = numRows - 1 + j*(numRows + 1)
            if letter_index < string_length:
                result += s[letter_index]
            else:
                break
        return(result)


