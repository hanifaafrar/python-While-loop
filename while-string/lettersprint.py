name = input('Enter Name: \n')
name1 = len(name)
index = 0
while index < name1:
    if name[index] in ['a', 'e', 'i', 'o', 'u']:
        print(name[index] , end=' ')
    index = index + 1