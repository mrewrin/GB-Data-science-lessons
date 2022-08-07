n = int(input('Please, enter a number to calculate the formula "n+nn+nnn": '))
result = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print ("Total: ", result)