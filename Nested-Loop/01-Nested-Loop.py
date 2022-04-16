#Outer loop will decide the count of rows
row = 1
while row <= 3:
#Inner loop will decide the count of column
    col = 1
    while col <= 5:
        print(col, end='')
        col = col + 1
    print()
    row = row + 1