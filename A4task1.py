try:
    with open('sample.txt','r+') as fyl:
        print(fyl.readline())
        print(fyl.readline())

except FileNotFoundError:
    print('Error: The file \'sample.txt\' was not found')
