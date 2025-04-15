from solution import *

string = 'PAYPALISHIRING'
solution = Solution()

print("case 1")
print("solution =") 
print("PAHNAPLSIIGYIR")
answer = solution.convert(string, 3)
print(answer)
print(answer == "PAHNAPLSIIGYIR")
print("")

print("-------------------")
print("")

print("case 2")
print("solution =")
print("PINALSIGYAHRPI")
answer = solution.convert(string, 4)
print(answer)
print(answer == "PINALSIGYAHRPI")

print("case 3")
print("solution =")
print("A")
answer = solution.convert("A", 1)
print(answer)
print(answer == "A")
