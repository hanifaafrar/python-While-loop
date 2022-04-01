number = int(input('Enter a number:'))
value = 0
while value <= number:
    # We can add or change the values here
    if value % 3 == 0 or value % 2 == 0:
        print(value)
    value = value + 1
print('End')