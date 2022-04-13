number = int(input('Enter Number: \n'))
count = 1

#while number > 0:
#    print(number)
#    count = count * number
#    number = number - 1
#print('Your total count is', count)


#Total count program using for loop
for no in range(1, number + 1):
    print(no)
    count = count * no
print('Total count is', count)