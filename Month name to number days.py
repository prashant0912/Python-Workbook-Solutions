import random
r = random.randint(28, 29)
word = input("Enter the name of month:")
if word =="January":
    print(30)
elif word =="February":
    print(r)
elif word =="March":
    print(31)
elif word == "April":
    print(30)
elif word =="May":
    print(31)
elif word =="June":
    print(30)
elif word=="July":
    print(31)
elif word=="August":
    print(30)
elif word =="September":
    print(30)
elif word =="October":
    print(31)
elif word =="November":
    print(30)
elif word =="December":
    print(31)
else:
    print("Not a month")

