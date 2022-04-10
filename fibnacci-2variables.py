#If we can take 1st as zero(0) , then the program avoid to print the zero and one twise.

first = -1 #1 0 1 1 2 3 5 8
second = 1 #0 1 1 2 3 5 8 13
#total = +  1 1 2 3 5 8 13 21

count = int(input('Enter Count: \n'))

while count > 0:
    print(first + second)
    second = first + second
    first = second - first
    count = count -1