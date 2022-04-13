sentance = input('Enter sentance: \n')
count = 1
for words in sentance:
    if words == ' ':
        count = count + 1
    print(words, end='')
print('\nYour total words count is', count)