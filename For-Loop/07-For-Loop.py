f,s = 0,1
count = int(input('Enter Count: \n'))

#while count > 0:
#    t = f + s
#    f = s
#    s = t
#    count = count - 1
#    print(t)

#fibnacci serias program with for loop
for no in range(count):
    t = f + s
    f = s
    s = t
    print(t)