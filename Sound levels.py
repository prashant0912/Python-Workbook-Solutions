n = int(input("Enter the sound in decibal:"))
if n == 130:
    print("It's a noise of Jackhammer")
elif n == 106:
    print("It's a noise of Gas lawnmower")
elif n == 70:
    print("It's a noise of Alarm clock")
elif n==40:
    print("It's a noise of Quietroom")
elif  106 <= n <= 130:
    print("Noise between  jackhammer and Gas lawnmower")
elif  70<=n<=106:
    print("Noise between  alarm clock  and Gas lawnmower ")
elif  40<=n<=70:
    print(" Noise between Quietroom and Alarm clock ")
elif n<40:
    print("Noise less than quiet room")
else:
    print("Noise greater than jackhammer")



