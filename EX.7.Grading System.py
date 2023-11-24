#taking the score as input

score = int(input('Enter score: '))
#if score greater than or equal to 70

if score >= 70:
    print('Grade A')

#if score greater than or equal to 60

elif score >= 60:
    print('Grade B')

#if score greater than or equal to 50
elif score >= 50:
    print('Grade C')

#if score greater than or equal to 40
elif score >= 40:
    print('Grade D')

#if score greater than or equal to 30
elif score >= 30:
    print('Grade E')

#if score less than 30
elif score < 30:
    print('Grade F')