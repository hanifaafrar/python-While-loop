number = int(input('Enter Number: \n'))
value = 0
count = 0
while value <= number:
    print(value, end=' ')
    count = count + value
    value = value + 1
print('\nYour total count is', count)
print('End')