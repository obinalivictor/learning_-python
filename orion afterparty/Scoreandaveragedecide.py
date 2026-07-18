
score1 = int(input("input score"))
score2 = int(input("input score"))
score3 = int(input("input score"))	
average = (score1 + score2 + score3)/3 
 
 
 
if (90 <= average <= 100):
	print("A")
elif (80 <= average < 90):	
	print("B")	
elif (70 <= average <80): 
	print("C") 
elif (60 <= average < 70):
	print("D")	
elif (0 <= average < 60): 
	print("F") 
	
print("average of the totl score is: ",average)
