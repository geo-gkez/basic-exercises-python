fname = input('Enter File: ')

if len(fname) <1 : fname ='clown.txt'
text = open(fname)

data = text.read()

counts=dict()

for character in data:
    if character not in counts:
        counts[character] = 1
    else :
        counts[character] += 1

print(counts)
