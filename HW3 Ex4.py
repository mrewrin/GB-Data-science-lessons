def my_function(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >=0:
            return 'Invalid input! x must be > 0, y < 0'
        else:
            result = 1
            for _ in range(abs(y)):
                result /= x
            print('The result of raising x to the power of y: ')
            return round(result, 6)
    except ValueError:
        return 'Invalid input! Enter a numerical value!'
num1 = input('Please enter a valid positive number: ')
num2 = input('Please enter a Please enter a negative integer: ')
print(my_function(num1, num2))
