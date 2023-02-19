# import necessary modules 
import robot_model
import math
import numpy as np

# set print formatting
np.set_printoptions(precision = 2, suppress = True)

# test 1
# set parameters for 1st link
alpha1= 1
theta1 = math.pi/2
a1 = 0
d1 = 0.1625

#set parameters for second link
alpha2 = 1
theta2 =math.pi/2
a2 = -0.425
d2 = 0

# call kinematic chain function with 2D array of the dh parameters 
H = robot_model.kinematic_chain([[a1,alpha1,d1,theta1],[a2, alpha2,d2,theta2]])

# call get_pos and pass H from kinematic chain function to determine x,y,and z locations
pos = robot_model.get_pos(H)
print(pos)

# call get_rot and pass H from kinematic function to determine roll-pitch-yaw
# angle values 
rot = robot_model.get_rot(H)
print(rot)
