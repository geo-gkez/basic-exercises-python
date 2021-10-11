list_1=[]
for number in range(0,100):
    if number % 2 == 0:
        list_1.append(number)

print(list_1)     


print()
print('Comprehension ')
print('First example')

list_2=[number for number in range(0,100) if number % 2 == 0]
print(list_2)

print()
print('Second example')
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

print(times_tables() )
print([ j*i for i in range(10) for j in range(10)])

print()
print('Third example')
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

correct_answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]


print(correct_answer[:10] ) # Display first 50 ids