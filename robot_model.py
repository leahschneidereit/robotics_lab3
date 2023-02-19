# import necessary modules
import numpy as np
import math

def dh_transformation (a, alpha, theta, d):
    '''
    Calculates the homogeneous transformation matrix for a single set of params
    parameters: a, alpha, theta, d
    returns: homogenous transformation matrix
    '''
    transformation = np.array([[math.cos(theta),-math.sin(theta)*math.cos(alpha),
                                math.sin(theta)*math.sin(alpha),a * math.cos(theta)],
                               [math.sin(theta),math.cos(theta)*math.cos(alpha),-math.cos(theta)*math.sin(alpha),
                                a * math.sin(theta)],[0, math.sin(alpha), math.cos(alpha),d],[0,0,0,1]])
    return transformation

def kinematic_chain (dh_params):
    '''
    Calculates the homogeneous transformation matrix for kinematic chain
    parameters: list of lists of dh_params in this order: a, alpha, d, theta
    returns: final array for the kinematic chain
    '''
    H = np.identity(4)
    for row in dh_params:
        a = row[0]
        alpha = row[1]
        d = row[2]
        theta = row[3]
        H_i = np.array([[math.cos(theta),-math.sin(theta)*math.cos(alpha),
                     math.sin(theta)*math.sin(alpha),a * math.cos(theta)],
                    [math.sin(theta),math.cos(theta)*math.cos(alpha),-math.cos(theta)*math.sin(alpha),
                     a * math.sin(theta)],[0, math.sin(alpha), math.cos(alpha),d],[0,0,0,1]])
        H = np.matmul(H, H_i)
    return H

def get_pos(trans_matrix):
    '''
    Extracts x,y,z position values from the transformation matrix
    parameters: transformation matrix
    returns: (x,y,z)
    '''
    h14 = trans_matrix.item(0,3)
    h24 = trans_matrix.item(1,3)
    h34 = trans_matrix.item(2,3)
    return h14, h24, h34

def get_rot(trans_matrix):
    '''
    Calculates roll, pitch, yaw rotation angle values
    parameters: transformation matrix
    returns: psi, theta, and phi values
    '''
    h11 = trans_matrix.item(0,0)
    h21 = trans_matrix.item(1,0)
    h31 = trans_matrix.item(2,0)
    h32 = trans_matrix.item(2,1)
    h33 = trans_matrix.item(2,2)

    psi = np.arctan(h32/h33)
    theta = np.arctan(-h31 / (math.sqrt(h32**2+h33**2)))
    phi = np.arctan(h21/h11)

    return psi, theta, phi
    


