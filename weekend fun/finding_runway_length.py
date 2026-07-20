acceleration = int(input("enter airplane acceleration"))
take_off_speed = float(input("enter take off speed"))
minimum_runway_length = int((acceleration * acceleration) / (take_off_speed + take_off_speed))

print("the minimum runway length for the airplane length is: ",minimum_runway_length)

