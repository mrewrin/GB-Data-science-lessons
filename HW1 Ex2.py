time = int(input('Please, enter time in seconds: '))
hour = time // 3600
minute = (time - hour * 3600) // 60
second = time - (hour * 3600 + minute * 60)
print("Converted the time for you in the usual format: {:02}:{:02}:{:02}".format(hour, minute, second))