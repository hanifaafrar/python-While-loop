name = input('Enter Name: \n')
name1 = len(name)
index = 0
while index < name1:
    if name[index]  in 'a':
        print(name , end=' ')
        break
    index = index + 1