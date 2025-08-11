def record(name='<desconhecido>', goals=0):
    print(f'The player {name} scored {goals} goals')

input_name = str(input("What's name of player?: ")).lower().strip()
input_goals = str(input('How many goals did the player score?: '))
if input_goals.isnumeric():
    input_goals = int(input_goals)
else:
    input_goals = 0

if input_name.strip() == '':
    record(goals=input_goals)
else:
    record(input_name, input_goals)

