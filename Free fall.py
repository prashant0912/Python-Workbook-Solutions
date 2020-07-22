import math
vi = float(input("Enter the initial speed in m/s:"))
d = float(input("Enter the distance in m:"))
vj = vi**2 + 2 * 9.8 * d
speed = math.sqrt(vj)
print(f"Speed = {speed}")

