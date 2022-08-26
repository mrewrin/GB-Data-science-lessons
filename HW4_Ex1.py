def pay():
    try:
        time = float(input('Hours of production: '))
        pay = int(input('Rate: '))
        bonus = int(input('Prize: '))
        res = time * pay + bonus
        print(f'Employee pay: {res}')
    except ValueError:
        return print('Not a number')
pay()
