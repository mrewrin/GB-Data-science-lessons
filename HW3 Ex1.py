def div(*args):
    try:
        argument_1 = int(input("Input dividend: "))
        argument_2 = int(input("Input divider: "))
        result = argument_1 / argument_2
    except ValueError:
        return 'Value error!'
    except ZeroDivisionError:
        return "Wrong devider! You can't use zero as a devider!"
    return result
print(f'Result - {div()}')
