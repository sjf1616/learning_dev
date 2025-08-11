value_house = float(input('How much this house?: '))
buyer_salary = float(input('How is your salary?: '))
year_to_pay = float(input('How when do you pay this house?: '))

installment = value_house / year_to_pay

if installment >= (30 * buyer_salary) / 100:
    print(f'\033[31mCredit refused')
else:
    print(f'\033[32mCredit approved')