from morse.builder import *
# adds a default robot (the MORSE mascott!)
robot = ATRV()

pose = Pose()
pose.add_interface('socket')
robot.append(pose)
motion = Waypoint()
motion.add_interface('socket')
robot.append(motion)



# # creates a new instance of the actuator
# pa10 = PA10()
# pa10.add_interface('socket')
# robot.append(pa10)
# # place your component at the correct location
# pa10.translate(0, 0, 0.9)
# pa10.rotate(0, 0, 0)

# armature = Armature(model_name = "pa_10")


depthvideocamera = DepthCamera()
depthvideocamera.translate(x=0, y=0, z=0.9)
depthvideocamera.properties(cam_width=101,cam_height=101,retrieve_zbuffer = True)
depthvideocamera.add_interface('socket')
robot.append(depthvideocamera)


semanticL = SemanticCamera()
semanticL.translate(x=0.2, y=0.3, z=0.9)
robot.append(semanticL)
semanticL.properties(cam_far=800)
semanticL.add_stream('socket')


env = Environment('robarch')
# env.select_display_camera(semanticL)
env.select_display_camera(depthvideocamera)