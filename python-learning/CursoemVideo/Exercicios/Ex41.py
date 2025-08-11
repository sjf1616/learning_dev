import datetime

yob = int(input('What is your year of birth:' ))
today = datetime.date.today().year

i = today - yob

if i <= 9:
    print('MIRIM')
elif i <= 14:
    print('INFANTIL')
elif i <= 19:
    print('JUNIOR')
elif i <= 25:
    print('SENIOR')
else:
    print('MASTER')