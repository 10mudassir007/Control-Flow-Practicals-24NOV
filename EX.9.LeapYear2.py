#taking year as input
x = int(input('Enter Year to identify: '))
#checking through modulus whether leap year or not
if x % 4 == 0:
    print(f'{x} is a leap year')
elif x % 4 != 0:
    print(f'{x} is not a leap year')