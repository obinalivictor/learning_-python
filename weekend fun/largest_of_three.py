#collect three integers
# by default the first integer is the largest number
# then any number greater than the first is the largest

number_one = int(input("enter integer"))

largest = number_one

number_two = int(input("enter integer"))

number_three = int(input("enter integer"))

if(number_two > largest):
	largest = number_two
if(number_three > largest):	
	largest = number_three
	
	
print("the largest number is: ",largest)
