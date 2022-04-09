f,s = 0,1
count = int(input('Enter Count: \n'))
while count > 1:
    t = f + s
    print(t, end=' ')
    f = s
    s = t
    count = count -1
print('end')