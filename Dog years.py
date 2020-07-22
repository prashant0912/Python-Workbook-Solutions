n = int(input("Enter the human years to convert into dog years:"))
if n<=2:
    dog_years = n*10.5
    print("dog years =", dog_years)
elif n>2:
    dog_years1 = ((2*10.5)+((n-2)*4))
    print("dog years:", dog_years1)




