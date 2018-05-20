import pymorse
import struct
import string
import numpy as np
import argparse
import random
import time

from pythonosc import osc_message_builder,osc_bundle_builder
from pythonosc import udp_client

###setup osc client
client = udp_client.SimpleUDPClient("127.0.0.1", 1238)

def print_pos(pose):
    print("I'm currently at %s" % pose)
    

def probedata(probe):
    print("probing %s" % probe)
    # bundle = osc_bundle_builder.OscBundleBuilder(osc_bundle_builder.IMMEDIATELY)
    # msg = osc_message_builder.OscMessageBuilder(address="/probe/data")
    # msg.add_arg(probe['x'])
    # bundle.add_content(msg.build())
    # msg.add_arg(probe['y'])
    # bundle.add_content(msg.build())
    # msg.add_arg(probe['z'])
    # bundle.add_content(msg.build())
    # msg.add_arg(probe['distance'])
    # bundle.add_content(msg.build())
    # msg.add_arg(probe['probevalue'])
    # bundle.add_content(msg.build())
    # msg.add_arg(probe['color'])
    # bundle.add_content(msg.build())
    # bundle = bundle.build()
    # print(dir(client))
    # client.send(msg)
    client.send_message("/probe/x", probe['x'])
    client.send_message("/probe/y", probe['y'])
    client.send_message("/probe/z", probe['z'])
    client.send_message("/probe/distance", probe['distance'])
    client.send_message("/probe/value", probe['probevalue'])
    client.send_message("/probe/color", probe['color'])

def depthdata(data):
    print(data['points'])
    # v = memoryview(data['points'].encode())
    # print(bytes(v[0:16]))
    # print(v)  ####<memory at 0x107f21108>
    # x = np.fromstring(data['points'], dtype='>f2')
    # print(x)

    # print(data)
    # print(struct.unpack_from('f', data['points'].encode(), 12 )) ##(9.126204533022451e+23,)
    # print(struct.unpack('f', data['points'].encode()))
    # print("test")


def startScan():
    with pymorse.Morse() as simu:
        simu.robot.arm.probeviz.subscribe(probedata)

        # print(simu.robot.arm.depthvideocamera.get_properties())
        # print(dir(simu.robot.arm))
        # print(simu.robot.pa10.get_joints())
        # print(simu.robot.arm.get_IK_limits("kuka_1"))
        # print(simu.robot.arm.get_IK_limits("kuka_2"))
        # move_IK_target(name, translation, rotation, relative, linear_speed, radial_speed) (non blocking)
        for x in range(100):
            # simu.robot.arm.move_IK_target('ik_target.robot.arm.kuka_7', [0.2,0.05*x,0.7], [0.0,0.0,0.0], False, 1,1 )
            # simu.robot.arm.place_IK_target('ik_target.robot.arm.kuka_7', [0.02,0.05*x,0], [0.0,0.0,0.0], True)
            simu.robot.arm.rotate("kuka_1", 0, 1)
            simu.sleep(1)
            for y in range(100):
                # simu.robot.arm.set_rotations(x*0.01, y*0.01, 0,0,0,0,0)
                # simu.robot.pa10.set_rotation_array(x*0.01,y*0.01,0,0,0)
                simu.robot.arm.set_rotation("kuka_2", x*0.01)
                simu.robot.arm.set_rotation("kuka_1", y*0.01)
                # simu.robot.arm.depthvideocamera.capture(1)
                # print(simu.robot.arm.depthvideocamera.get_local_data())
                # simu.robot.arm.depthvideocamera.subscribe(depthdata)
                # probe_value()
                simu.sleep(0.1)
        # simu.robot.arm.armpose.subscribe(print_pos)
        # simu.robot.arm.move_IK_target('ik_target.robot.arm.kuka_7', [0.2,0.111,1], [0.0,0.0,0.0], False, 0.1,0.1 )
        # simu.sleep(1)
        # simu.armpose.subscribe(print_pos)

def set_horizontal():
    with pymorse.Morse() as simu:
        simu.robot.arm.set_rotation("kuka_2", -3.14/4)
        simu.robot.arm.set_rotation("kuka_4", 3.14/4)
        
        simu.robot.arm.depthvideocamera.capture(-1)
        simu.robot.arm.depthvideocamera.subscribe(depthdata)
        


# def probe_value():
#     with pymorse.Morse() as simu:
#         simu.robot.arm.probeviz.subscribe(probedata)
#         # simu.robot.arm.armpose.subscribe(print_pos)
#         while True:
#             # simu.robot.arm.probeviz.get_local_data()
#             # simu.robot.arm.probeviz.subscribe(probedata)
#             # simu.robot.arm.probeviz.publish({"test": 45})
# # set_horizontal()



startScan()