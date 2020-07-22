n = int(input("Enter the number of loaves you want to buy:"))
price = n*3.49
discount = ((60/100)*price)
price1 = price - discount
print("Regular price = $",round(price, 2))
print("one day old bread discount =$", round(discount, 2))
print("Total payable price =$", round(price1, 2))


