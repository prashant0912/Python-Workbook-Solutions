side1 = input("Enter the 1st side of triangle:")
side2 = input("Enter the 2nd side of triangle:")
side3 = input("Enter the 3rd side of triangle:")
if side1 == side2 == side3:
    print("It's an equilateral triangle ")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("It's an isosceles triangle ")
else:
    print("It's a scalene triangle")

