#taking both number as input
num1 = int(input('Enter number 1 : '))
num2 = int(input('Enter number 2 : '))

#if num 1 is greater than num2
if num1 > num2:
    print(f'{num1} is greater than {num2}')
#if num 2 is greater than num 1
elif num2 > num1:
    print(f'{num2} is greater than {num1}')
#if both are equal
else:
    print('Both numbers are equal')