days = int(input("Enter the time in days:"))
hour = int(input("Enter the time in hours:"))
minutes = int(input("Enter the time in minutes:"))
seconds = int(input("Enter thetime in seconds:"))


second_in_days = days * 86400
second_in_hours  =  hour * 3600
second_in_min = minutes * 60
total = second_in_days+second_in_hours+second_in_min + Second

print(f"{total} seconds")

