time = int(input("Enter the time in seconds:"))
days = time//(24*3600)
time = time % (24*3600)
Hours = time//3600
time = time % 3600
minutes = time//60
time = time % 60
seconds = time

print(f"{days}:{Hours}:{minutes}:{seconds}")



