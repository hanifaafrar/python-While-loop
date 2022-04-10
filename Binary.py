#rem = number(7) % 2  == 1
#number = number(7) // 2  == 3

#rem = number(3) % 2  == 1
#number = number(3) // 2  == 1

#rem = number(1) % 2  == 1
#number = number(1) // 2  == 0

number = int(input('Enter Number: \n'))
word = ' '

while number > 0:
    rem = number % 2
    word = str(rem) + word
    number = number // 2
    #print(rem, end='')
print(word)





