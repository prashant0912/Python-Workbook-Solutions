import math
a = float(input("Enter the latitude of Ist point:"))
b = float(input("Enter the latitude  of 2nd  point:"))
c = float(input("Enter the longitude of Ist point:"))
d = float(input("Enter the longitude of 2nd point:"))
change1 = math.radians(a)
change2 = math.radians(b)
change3 = math.radians(c)
change4 = math.radians(d)
distance = 6371.01 * math.acos(math.sin(change1) * math.sin(change2) + math.cos(change1) * math.cos(change2)
                               * math.cos(change3-change4))
print(f"The distance between the two points on earth is {distance}")


