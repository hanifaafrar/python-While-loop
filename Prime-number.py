number = int(input('Enter Number: \n'))
div = 2
while number > div:
    if number % div == 0:
        print('Not Prime Number')
        break
    div = div + 1
else:
    print('Prime Number')