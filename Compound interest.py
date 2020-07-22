p = float(input("Enter the principal:"))
r = int(input("Enter the rate of return:"))
t = int(input("Enter the time:"))
interest = (p*r*t)/100
Amount = p + interest
interest1 = (Amount*r*t)/100
Amount1 = Amount+interest1
interest2 = (Amount1*r*t)/100
Amount2 = Amount1 + interest2
print(f"In Ist year amount ={Amount}")
print(f"In 2nd year amount = {Amount1}")
print(f"In 3rd year amount = {Amount2}")







