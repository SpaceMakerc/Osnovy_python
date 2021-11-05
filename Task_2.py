user_time = int(input('Write the time in the second: '))
time_in_minutes = 0
seconds = 0
hours = 0
minutes = 0

if user_time > 60:
    time_in_minutes = user_time // 60
    seconds = user_time % 60
    if time_in_minutes > 60:
        hours = time_in_minutes // 60
        time_in_minutes = time_in_minutes % 60
else:
    seconds = user_time
    time_in_minutes = user_time // 60

print(f'User time is {hours:02}:{time_in_minutes:02}:{seconds:02}')
