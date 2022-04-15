number = int(input('Enter Number: \n'))
#div = 2

#while number > div:
#    if number % div == 0:
#       print('Not Prime')
#        break
#    div = div + 1
#else:
#    print('Prime')


#Prime Number with for loop
for no in range(2, number):
    if number % no == 0:
        print('Not Prime')
        break
else:
    print('Prime')