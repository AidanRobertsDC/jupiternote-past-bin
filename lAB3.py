import math
import numpy as np
import roboticstoolbox as rtb

'''
Add your code in this cell for step 1
'''

# load the gen 3 lite robot model from the robot toolbox
# the DH parameters where sourced from the user manual for the Kinova gen 3 lite robot manipulator
gen3_lite = rtb.DHRobot(
    [
        # Add a list of joint definitions using the DH parameters
        # for the Kinova gen 3 lite robot manipulator
        # for example:
        #
        # rtb.RevoluteDH(d = 0.243, alpha = math.radians(90), a = 0),
        # etc...
        #
        # there are 6 joints in total
        
        rtb.RevoluteDH(
            d = (128.25+115),
            alpha = math.radians(90),
            a = 0,
            # note that the dimensions are in m instead of mm
            
        ),
        rtb.RevoluteDH(
            d = 30,
            alpha = math.radians(180),
            a = 280,
            
        ),
        rtb.RevoluteDH(
            d = 20,
            alpha = math.radians(90),
            a = 0,
            # note that the dimensions are in m instead of mm
            
        ),
        rtb.RevoluteDH(
            d = (140+105),
            alpha = math.radians(90),
            a = 0,
            
        ),
        rtb.RevoluteDH(
            d = (28.5+28.5),
            alpha = math.radians(90),
            a = 0,
            
            
        ),
        rtb.RevoluteDH(
            d = (105+130),
            alpha = math.radians(0),
            a = 0,
            
        )
    ],
    name = "gen3_lite"
)

print(gen3_lite)

# plot the robot model with some example joint angles
# an example with the same angles in j1, j3, j4, and j6


# create the joint angles array
# q = np.array([0, 0, 0, 0, 0, 0])
q = np.array([52+90, 2.7+90, 90+90, 98+90, 78+180, 328+90])

# plot the arm
gen3_lite.plot(q, limits=[-0.4, 0.4, -0.4, 0.4, -0.6, 0.6])
