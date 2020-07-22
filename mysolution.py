def seconds_to_days(seconds):
    minutes = seconds // 60
    print(f'minutes = {minutes}')
    sec = seconds % 60
    hours = minutes // 60
    mins = minutes % 60
    days = hours // 24
    hrs = hours % 24
    print(f'{days} days {hrs} hrs {mins} minutes {sec} seconds')


while True:
    time_in_seconds = int(input('Enter time in seconds:'))
    seconds_to_days(time_in_seconds)