number = int(input('Enter No: \n'))
n = 0
while n <= number:
    if number % 3 == 0:
        print(n)
    n = n + 3
print('End')