#The binary value equal to 7
#  1   1   1
# 2^2 2^1 2^0
# 4    2   1  == 7

# The binary value equal to 10
#  1    0    1    0
# 2^3  2^2  2^1  2^0
#  8    0    2    0   == 10

import math
number = int(input('Enter Number: \n'))
total = 0
i = 0

while number > 0:
    rem = number % 10
    value = rem * int(math.pow(2,i)) # used the "i" to add the power #
    total = total + value
    number = number // 10
    i = i + 1
print(total)
    #print(rem, number, value, total)


# this program is very long so, here we want a loop