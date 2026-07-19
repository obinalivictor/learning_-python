number_one = int(input("enter integer: "))
number_two = int(input("enter integer: "))

if(number_one > 0 and number_two > 0):
	print("q1")

elif(number_one < 0 and number_two > 0):
	print("q2")

elif(number_one < 0 and number_two < 0):
	print("q3")

elif(number_one > 0 and number_two < 0):
	print("q4")
	
elif(number_one == 0 and number_two == 0):	
	print("origin")
	
elif(number_two == 0 and number_one != 0):	
	print("x-axis")
	
elif(number_one == 0 and number_two != 0):	
	print("y-axis")
	
	
