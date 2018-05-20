# import pymorse

# def print_pos(pose):
#     print("I'm currently at %s" % pose)

# with pymorse.Morse() as simu:

#     # subscribes to updates from the Pose sensor by passing a callback
#     simu.robot.pose.subscribe(print_pos)

#     # sends a destination
#     # simu.robot.motion.publish({'x' : 10.0, 'y': 5.0, 'z': 0.0,
#     #                           'tolerance' : 0.5,
#     #                           'speed' : 1.0})

#     # Leave a couple of millisec to the simulator to start the action
#     simu.sleep(0.1)

#     # waits until we reach the target
#     while simu.robot.motion.get_status() != "Arrived":
#         simu.sleep(0.5)

#     print("Here we are!")


import pymorse
import struct
import string
import numpy as np

def print_pos(pose):
    print("I'm currently at %s" % pose)

def depthdata(data):
    # print(data['points'])
    v = memoryview(data['points'].encode())
    print(bytes(v[0:16]))
    print(v)  ####<memory at 0x107f21108>
    x = np.fromstring(data['points'], dtype='>f2')
    print(x)

    print(data)
    print(struct.unpack_from('f', data['points'].encode(), 16 )) ##(9.126204533022451e+23,)
    # print(struct.unpack('f', data['points'].encode()))
    # print("test")

with pymorse.Morse() as simu:

    ###configure depth camera
    # simu.robot.depthvideocamera.set_property('cam_width', 1)
    # simu.robot.depthvideocamera.set_property('cam_height', 1)
    print(simu.robot.pa10.list_IK_targets())
    print(simu.robot.arm.list_IK_targets())

    # subscribes to updates from the Pose sensor by passing a callback
    simu.robot.pose.subscribe(print_pos)
    # simu.robot.arm.arm_pose.subscribe(print_pos)
    # sends a destination
    simu.robot.motion.publish({'x' : 4.0, 'y': 0.0, 'z': 0.0,
                              'tolerance' : 0.5,
                              'speed' : 1.0})

    # simu.robot.pa10.set_rotation_array(1,1,0,-1,0)
    simu.robot.depthvideocamera.subscribe(depthdata)
    # Leave a couple of millisec to the simulator to start the action
    simu.sleep(0.1)
    # simu.robot.depthvideocamera.capture(1)
    # print(simu.robot.depthvideocamera.get('points'))
    # waits until we reach the target
    while simu.robot.motion.get_status() != "Arrived":
    # while True:
        simu.robot.depthvideocamera.capture(-1)
        simu.sleep(0.5)

    print("Here we are!")
    