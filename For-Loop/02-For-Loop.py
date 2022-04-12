number = int(input('Enter Number: \n'))
total = 0
#count = 0

#while number >= count:
#    print(count)
#    total = total + count
#    count = count + 1
#print('your total is', total)

#addition program with for loop
for no in range(1, number + 1):
    print(no, end=' ')
    total = total + no
print('your total is', total)