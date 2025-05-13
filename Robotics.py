import numpy as np
import scipy
import matplotlib.pyplot as plt
import roboticstoolbox as rtb
import spatialmath as sm

from roboticstoolbox.models.DH import Puma560
import spatialmath as sm
import numpy as np

# Create a Puma560 robot model
robot = Puma560()

# Define a joint configuration
q = np.array([0, np.pi/4, -np.pi/4, 0, np.pi/2, 0])

# Compute Forward Kinematics
T = robot.fkine(q)
print("End-effector transformation matrix:\n", T)

# Plot the robot in 3D
robot.plot(q)
