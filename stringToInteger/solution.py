

class Solution():
    def myAtoi(self, s: str) -> int:
        number_dict = {
                "0": 0,
                "1": 1,
                "2": 2,
                "3": 3,
                "4": 4,
                "5": 5,
                "6": 6,
                "7": 7,
                "8": 8,
                "9": 9,
        }

        result = 0
        is_int = False
        is_negative = False

        for i in s:
            if "-" == i and is_negative == False and is_int == False:
                is_negative = True
            elif " " == i and is_negative == False and is_int == False:
                next
            elif i in number_dict:
                result *= 10
                result += number_dict[i]
                is_int = True
            else:
                break
        
        if is_negative:
            result *= -1

        return result
            

