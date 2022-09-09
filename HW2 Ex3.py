season_list = ['Winter', 'Spring', 'Summer', 'Autumn']
season_dict = dict(key_1='Winter', key_2='Spring', key_3='Summer', key_4='Autumn')
n_month = int(input('Please, enter number of month: '))
if n_month == 12 or n_month == 1 or n_month == 2:
    print(season_list[0])
    print(season_dict.get('key_1'))
elif n_month == 3 or n_month == 4 or n_month == 5:
    print(season_list[1])
    print(season_dict.get('key_2'))
elif n_month == 6 or n_month == 7 or n_month == 8:
    print(season_list[2])
    print(season_dict.get('key_3'))
elif n_month == 9 or n_month == 10 or n_month == 11:
    print(season_list[3])
    print(season_dict.get('key_4'))
else:
    print('You entered an invalid month number')
