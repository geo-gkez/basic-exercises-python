for i in 'hello':
    if(i == 'e'):
        print('pass executed')
        pass
    print(i)

print('----')

for i in 'hello':
    if(i == 'e'):
        print('continue executed')
        continue
    print(i)