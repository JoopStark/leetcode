class Solution:
    def convert(self, s: str, numRows: int) -> str:
        string_length = len(s)
        full_columns = 2*numRows - 2
        if numRows == 1:
            result = s
        else:
            result = ""

            for j in range(0,string_length):
                letter_index = j*(full_columns)
                if letter_index < string_length:
                    result += s[letter_index]
                else:
                    break
            # print(result)
            for i in range(1, numRows - 1):
                if i < string_length:
                    result += s[i]
                else:
                    break
                for j in range(1, string_length):
                    letter_index = i + j*(full_columns)
                    letter_index_minus = letter_index - (i * 2)
                    print(letter_index)
                    if letter_index_minus < string_length:
                        result += s[letter_index_minus]
                    else:
                        break
                    if letter_index < string_length:
                        result += s[letter_index]
                    else:
                        break


            for j in range(0, string_length):
                letter_index = numRows - 1 + j*(full_columns)
                if letter_index < string_length:
                    result += s[letter_index]
                else:
                    break
        return(result)


