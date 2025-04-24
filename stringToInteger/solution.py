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
        sign_count = 0

        for i in s:
            if "-" == i and sign_count == 0 and is_int == False:
                is_negative = True
                sign_count += 1
            elif " " == i and sign_count == 0 and is_int == False:
                next
            elif "+" == i and sign_count == 0 and is_int == False:
                sign_count += 1
                next
            elif i in number_dict:
                result *= 10
                result += number_dict[i]
                is_int = True
            else:
                break

        if is_negative and result > (2 ** 31):
            result = (2 ** 31)
    
        if is_negative == False and result > ((2 ** 31) - 1):
            result = ((2 ** 31 ) -1)

        if is_negative:
            result *= -1

        return result
            

