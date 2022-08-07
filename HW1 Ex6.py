a = float(input("Enter your first day's run in km: "))
b = float(input("Enter the total desired result in km: "))
rd = 1
if b <= a:
    print('Error! The desired result is less than the result achieved on the first day!')
else:
    while a < b:
        a = a + 0.1 * a
        rd += 1
    print(f'You will get results in %d days' % rd)