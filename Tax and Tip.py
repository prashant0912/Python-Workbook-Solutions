amount = float(input("Enter the amount of food you ordered:"))
tip = (18/100)*amount
gst = (5/100)*amount
bill = amount + tip + gst

print(tip)
print(gst)




print(f"Total amount payable is {bill}")

