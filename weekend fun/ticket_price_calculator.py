# user input age 
# use if statement to calculate the ticket price
# if age lesser than five then print free

age = int(input("enter your age: "))
if(age < 5):
	print("ticket is free")
elif(age >= 5 and age <= 12):
	price = age * 5
	print("your ticket price is: ",price,"$")
elif(age >= 13 and age <= 64):
	price = age * 12
	print("your ticket price is: ",price,"$")
elif(age >= 65):
	price = age * 8
	print("your ticket price is: ",price,"$")
