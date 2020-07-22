import math
def area(s1,s2,s3):
    s = (s1+s2+s3)/2
    d = s*(s-s1)*(s-s2)*(s-s3)
    e = math.sqrt(d)
    return e

print(area(6,7,9))

