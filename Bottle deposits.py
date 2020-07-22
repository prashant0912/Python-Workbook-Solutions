bottle = int(input("Enter the number of bottles you want to deposit:"))
quantity = float(input("Enter the quantity of drink:"))
if quantity <= 1.0:
    amount = bottle*0.10
    print(f"You will receive ${round(amount,2)}")
elif quantity >= 1.0:
    amount1 = bottle*0.25
    print(f"You will receive ${round(amount1,2)}")



