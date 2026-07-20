number = int(input("enter a number from (1-7): "))
if(number > 7):
	print("invalid input")
	

elif(number == 1):
	print("sunday")

elif(number == 2):
	print("monday")

elif(number == 3):
	print("tuesday")

elif(number == 4):
	print("wednesday")

elif(number == 5):
	print("thursday")

elif(number == 6):
	print("friday")

elif(number == 7):
	print("saturday")
	
	
age = int(input("enter age: "))

if(age < 13):
	print("child")

elif(age >= 13 and age <= 19):
	print("teen")

elif(age >= 20):
	print("adult")


number = int(input("enter integer: "))
if(number % 5 == 0 and number % 3 == 0):	
	print("can be divided")
	
else:
	print("cannot be divided")

