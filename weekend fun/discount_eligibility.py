total_bill = int(input("input bill"))
is_member = input("enter yes or no")


if(total_bill >= 1000 and is_member == "yes"):
	print("10% off")

elif(total_bill >= 1000 and is_member == "no"):
	print("5% off")

else:
	print("no discount")







