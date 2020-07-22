import math
n = int(input("Enter the number of side:"))
s = int(input("Enter the length of side:"))

area = (n*(s*s))/(4*math.tan(math.pi/n))
print(area)



