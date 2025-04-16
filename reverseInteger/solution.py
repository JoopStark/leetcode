#

class Solution():
    def reverse(self, x: int) -> int:
        result = 0
        negative = False

        if x < 0:
            negative = True
            x *= -1

        while x > 0:
            result *= 10     
            result += x % 10
            x = x // 10
        
        if negative:
            result *= -1

        return result


