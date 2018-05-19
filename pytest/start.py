from morse.builder import *

robot = ATRV()
arm = KukaLWR()
arm.add_stream('socket')
arm.add_service('socket')
robot.append(arm)

motion = MotionVW()
motion.add_stream('socket')
robot.append(motion)
arm.translate(z=0.9)

pose = Pose()
pose.add_interface('socket')
robot.append(pose)



semanticL = SemanticCamera()
semanticL.translate(x=0.2, y=0.3, z=0.9)
robot.append(semanticL)
semanticL.properties(cam_far=800)


# semanticL.add_stream('socket')


# arm_pose = ArmaturePose()
# # the sensor is appended to the armature, *not* to the robot
# arm.append(arm_pose)



# # arm_pose.stream('socket')
# arm_pose.add_service('socket')
# # env = Environment('empty')


# arm.rotate(z=0.9)


# Environment
env = Environment('robarch')
env.select_display_camera(semanticL)



# from morse.builder import *

# # Add a robot with a position sensor and a motion controller
# robot = ATRV()

# pose = Pose()
# pose.add_interface('socket')
# robot.append(pose)

# arm = KukaLWR()
# robot.append(arm)
# arm.translate(z=0.9)
# #read arm positions
# arm_pose = ArmaturePose()
# arm_pose.add_interface('socket')
# arm.append(arm_pose)
# # write arm positions
# # armature = Armature(model_name = "kuka_lrw")
# armature = Armature(armature_name = "KukaLRW")
# armature.add_interface('socket')
# robot.append(armature)


# motion = Waypoint()
# motion.add_interface('socket')
# robot.append(motion)


# # Environment
# env = Environment('land-1/trees')