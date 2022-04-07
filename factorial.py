no1 = int(input('Enter NO1 \n'))
no2 = int(input('Enter NO2 \n'))
count = 2

big = no2 if no1 > no2 else no2

while count > 1:
    if big % no1 == 0 and big % no2 == 0:
        print(big)
        break
    big = big + 1
    count = count + 1