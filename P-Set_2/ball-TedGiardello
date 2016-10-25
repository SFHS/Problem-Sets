#TRACK THE POSITION OF A BALL THAT DOES NOT BOUNCE IN A THREE DIMENTIAL VACCUM 

g = 9.8 #m/s**2

initial_velocity_x = input("initial velocity: x component = ")

initial_velocity_y = input("initial velocity: y component = ")

initial_velocity_z = input("initial velocity: z component = ")

def position_x_component(t): #meters
	return initial_velocity_x * t

def position_y_component(t): #meters
	return initial_velocity_y * t

def position_z_component(t): #meters 
	return float((initial_velocity_z * t) - (g * t**2))

# def velocity_x_component(t): #meters/second
# 	return initial_velocity_x

# def velocity_y_component(t): #meters/second
# 	return initial_velocity_y

# def velocity_z_component(t): #meters/second
# 	return initial_velocity_z - (g * t)

# def acceleration_x_component(t): #m/s**2
# 	return 0

# def acceleration_y_component(t): #m/s**2
# 	return 0

# def acceleration_z_component(t): #m/s**2
# 	return -g

end_time = float(initial_velocity_z)/(g) #time at which the ball hits the ground

for i in range(int(end_time + 1)): #maybe adjust to 0.1 or 0.01 seconds, depends of parameters
	position = [position_x_component(i), position_y_component(i), position_z_component(i)]
	print(postion) #prints the 'x' 'y' and 'z' components at every second before the ball hits the ground