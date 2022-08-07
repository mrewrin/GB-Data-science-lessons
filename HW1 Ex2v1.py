time = int(input('Please, enter time in seconds: '))
hour = time // 3600
minute = (time - hour * 3600) // 60
second = time - (hour * 3600 + minute * 60)
print(f"Converted the time for you in the usual format: {hour:02}:{minute:02}:{second:02}")