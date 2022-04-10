#The binary value equal to 7
#  1   1   1
# 2^2 2^1 2^0
# 4    2   1  == 7

# The binary value equal to 10
#  1    0    1    0
# 2^3  2^2  2^1  2^0
#  8    0    2    0   == 10

import math
total = 0

rem = 1010 % 10
number = 1010 // 10
value = rem * int(math.pow(2,0))
total = total + value
print(rem, number, value, total)

rem = 101 % 10
number = 101 // 10
value = rem * int(math.pow(2,1))
total = total + value
print(rem, number, value, total)

rem = 10 % 10
number = 10 // 10
value = rem * int(math.pow(2,2))
total = total + value
print(rem, number, value, total)

rem = 1 % 10
value = rem * int(math.pow(2,3))
total = total + value
number = 1 // 10
print(rem, number, value, total)


# this program is very long so, here we want a loop