#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <roboarchsim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from roboarchsim.builder.robots import Kukabase
from roboarchsim.builder.sensors import Probeviz


robot = Kukabase()
arm = KukaLWR()
arm.add_stream('socket')
arm.add_service('socket')
robot.append(arm)

motion = MotionVW()
motion.add_stream('socket')
robot.append(motion)
arm.translate(z=0.3)
armpose = Pose()
armpose.add_interface('socket')
arm.append(armpose)


pose = Pose()
pose.add_interface('socket')
robot.append(pose)

# pa10 = PA10()
# pa10.add_interface('socket')
# robot.append(pa10)
# pa10.translate(0,0,0.3)



semanticL = SemanticCamera()
semanticL.translate(x=0.2, y=0.3, z=0.3)
robot.append(semanticL)
semanticL.properties(cam_far=800)

depthvideocamera = DepthCamera()
depthvideocamera.translate(x=0, y=0.0, z=1.28)
depthvideocamera.rotate(x=0, y=1.571, z=0)
depthvideocamera.properties(cam_width=100,cam_height=100,retrieve_zbuffer = True)
depthvideocamera.add_interface('socket')
arm.append(depthvideocamera)

probeviz = Probeviz()
probeviz.translate(x=0, y=0.0, z=1.28)
probeviz.rotate(x=0, y=1.571, z=0)
arm.append(probeviz)



# set 'fastmode' to True to switch to wireframe mode
env = Environment('robarch', fastmode = False)
# env.set_camera_location([-18.0, -6.7, 10.8])
# env.set_camera_rotation([1.09, 0, -1.14])
env.select_display_camera(depthvideocamera)
    
