# impot robot model module
import robot_model

#import math modules
import math
import numpy as np

#set print formatting
np.set_printoptions(precision = 1, suppress = True)


#--------------TEST 1---------------#
print("Test 1")
print()

# set dh parameters for 1st link
a1 = 1
alpha1= 0
theta1 = math.pi/2
d1 = 0

#set parameters for second link
a2 = 1
alpha2 = 0
theta2 = math.pi/2
d2 = 0

# call kinematic_chain to calculate homogeneous transformation matrix, H 
H = robot_model.kinematic_chain([[a1,alpha1,theta1,d1],[a2, alpha2,theta2,d2]])

# call get_pos and pass Hto determine x,y,and z values 
pos = robot_model.get_pos(H)
print("x,y,z: ", pos)

# call get_rot and pass H to determine roll-pitch-yaw angle values 
rot = robot_model.get_rot(H)
print("roll, pitch, yaw: ",rot)

#formatting
print()
print()

#----------------TEST 2-----------------#
print("Test 2")
print()

#set dh parameters for each link (1-6)
a1 = 0
alpha1= math.pi/2
theta1 = 0
d1 = .1625

a2 = -0.425
alpha2= 0
theta2 = 0
d2 = 0

a3 = -0.3922
alpha3= 0
theta3 = 0
d3 = 0

a4 = 0
alpha4= math.pi/2
theta4 = 0
d4 = 0.1333

a5 = 0
alpha5= -math.pi/2
theta5 = 0
d5 = 0.0997

a6 = 0
alpha6= 0
theta6 = 0
d6 = 0.0966

#call kinematic chain to determine final transformation matrix 
H = robot_model.kinematic_chain([[a1,alpha1,theta1,d1],[a2, alpha2,theta2,d2],[a3,alpha3,theta3,d3],
                                 [a4,alpha4,theta4,d4],[a5,alpha5,theta5,d5],[a6,alpha6,theta6,d6]])

# call get_pos and pass H to determine x,y,z values from transformation matrix
pos = robot_model.get_pos(H)
print("x,y,z: ", pos)

# call get_rot and pass H to determine roll, pitch, and yaw angle values
rot = robot_model.get_rot(H)
print("roll, pitch, yaw: ",rot)

#formatting
print()
print()

#-----------------Test 3--------------------#
print("Test 3")
print()

# theta2 is only value that changes from case1 - set new value for theta2
theta2 = -math.pi/2


#call kinematic chain to determine transformation matrix 
H = robot_model.kinematic_chain([[a1,alpha1,theta1,d1],[a2, alpha2,theta2,d2],[a3,alpha3,theta3,d3],
                                 [a4,alpha4,theta4,d4],[a5,alpha5,theta5,d5],[a6,alpha6,theta6,d6]])

# call get_pos and pass H to determine x,y,z position
pos = robot_model.get_pos(H)
print("x,y,z: ", pos)

# call get_rot and pass H to calculate roll-pitch-yaw angle values 
rot = robot_model.get_rot(H)
print("roll, pitch, yaw: ",rot)
