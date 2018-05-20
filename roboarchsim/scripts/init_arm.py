import pymorse
import struct
import string
import numpy as np
import argparse
import random
import time

from pythonosc import osc_message_builder,osc_bundle_builder
from pythonosc import udp_client

bigsensorvalue = False
###setup osc client
client = udp_client.SimpleUDPClient("127.0.0.1", 1238)

def print_pos(pose):
    print("I'm currently at %s" % pose)
    

def probedata(probe):
    global bigsensorvalue
    print("probing %s" % probe)
    client.send_message("/probe/x", probe['x'])
    client.send_message("/probe/y", probe['y'])
    client.send_message("/probe/z", probe['z'])
    client.send_message("/probe/distance", probe['distance'])
    client.send_message("/probe/value", probe['probevalue'])
    client.send_message("/probe/color", probe['color'])
    if probe['probevalue'] > 512:
        print("bigsensorvalue!")
        bigsensorvalue = True
        

def probedatalimits(probelimit):
    print("probing %s" % probelimit)

def startScan():
    with pymorse.Morse() as simu:
        simu.robot.arm.probeviz.subscribe(probedata)
        # print(simu.robot.arm.depthvideocamera.get_properties())
        # print(dir(simu.robot.arm))
        # print(simu.robot.pa10.get_joints())
        print(simu.robot.arm.get_IK_limits("kuka_1"))
        print(simu.robot.arm.get_IK_limits("kuka_2"))
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

def startRelativeScan(xpos, ypos):
    global bigsensorvalue
    with pymorse.Morse() as simu:
        simu.robot.arm.probeviz.subscribe(probedata)
        speed = 0.5
        for x in range(10):
            if bigsensorvalue:
                bigsensorvalue = False
                break
            simu.robot.arm.rotate("kuka_1", xpos, speed)
            simu.sleep(1)
            for y in range(10):
                if bigsensorvalue:
                    break
                simu.robot.arm.rotate("kuka_2", xpos+x*0.1, speed)
                simu.robot.arm.rotate("kuka_1", ypos+y*0.1, speed)
                simu.sleep(0.3)
    jump_to_new_scan()
    
def set_horizontal():
    with pymorse.Morse() as simu:
        simu.robot.arm.set_rotation("kuka_2", -3.14/4)
        simu.robot.arm.set_rotation("kuka_4", 3.14/4)
        simu.robot.arm.depthvideocamera.capture(-1)
        simu.robot.arm.depthvideocamera.subscribe(depthdata)
        
def jump_to_new_scan():
    xpos = (random.random()*2) - 1
    ypos = (random.random()*2) - 1
    with pymorse.Morse() as simu:
        simu.robot.arm.set_rotation("kuka_2", xpos) ##, 2 ) ### limits [-2.9670610427856445, 2.9670610427856445]
        simu.robot.arm.set_rotation("kuka_1", ypos )##, 2)  ### limits [-2.0943961143493652, 2.0943961143493652]
        simu.sleep(5)
        startRelativeScan(xpos,ypos)
        

def list_scan_limits():
    ## to better map the values of the scan in a 2D space it's usefull to get the bounds, as detected by this function
    with pymorse.Morse() as simu:
        speed = 2
        # simu.robot.arm.probeviz.subscribe(probedatalimits)
        simu.robot.arm.rotate("kuka_1", -2.0670610427856445, speed)
        simu.robot.arm.set_rotation("kuka_2", -1.5943961143493652)#, speed)
        print(simu.robot.arm.probeviz.get_local_data())
        simu.sleep(5)
        print(simu.robot.arm.probeviz.get_local_data())
        simu.robot.arm.rotate("kuka_1", -2.0670610427856445,speed)
        simu.robot.arm.rotate("kuka_2", 1.5943961143493652,speed)
        print(simu.robot.arm.probeviz.get_local_data())
        simu.sleep(5)
        print(simu.robot.arm.probeviz.get_local_data())
        simu.robot.arm.rotate("kuka_1", 2.0670610427856445,speed)
        simu.robot.arm.rotate("kuka_2", -1.5943961143493652,speed)
        print(simu.robot.arm.probeviz.get_local_data())
        simu.sleep(5)
        print(simu.robot.arm.probeviz.get_local_data())
        simu.robot.arm.rotate("kuka_1", 2.0670610427856445,speed)
        simu.robot.arm.rotate("kuka_2", 1.3943961143493652,speed)
        print(simu.robot.arm.probeviz.get_local_data())
        simu.sleep(5)                        
        print(simu.robot.arm.probeviz.get_local_data())

def moveTo4corners():
    cx = 0
    cy = 0
    cz = 0.6
    x1 = 0.4 
    y1 = -0.02
    z1 = 0.2
    x2 = x1
    y2 = -0.02
    z2 = -0.2
    x3 = x1
    y3 = 0.02
    z3 = -0.2
    x4 = x1
    y4 = 0.02
    z4 = 0.2
    with pymorse.Morse() as simu:
        # simu.robot.arm.probeviz.subscribe(probedata)
        # move_IK_target(name, translation, rotation, relative, linear_speed, radial_speed) (non blocking)
        simu.robot.arm.move_IK_target('ik_target.robot.arm.kuka_7', [cx+x1,cy+y1,cz+z1], [0.0,0.0,0.0], False, 1,1 )
        # simu.robot.arm.place_IK_target('ik_target.robot.arm.kuka_7', [cx+x1,cy+y1,cz+z1], [0.0,0.0,0.0], False)
        print(simu.robot.arm.probeviz.get_local_data())

        # simu.robot.arm.place_IK_target('ik_target.robot.arm.kuka_7', [0.02,0.05*x,0], [0.0,0.0,0.0], True)
        simu.sleep(3)
        simu.robot.arm.move_IK_target('ik_target.robot.arm.kuka_7', [cx+x2,cy+y2,cz+z2], [0.0,0.0,0.0], False, 1,1 )
        # simu.robot.arm.place_IK_target('ik_target.robot.arm.kuka_7', [cx+x2,cy+y2,cz+z2], [0.0,0.0,0.0], False )
        print(simu.robot.arm.probeviz.get_local_data())

        simu.sleep(3)
        simu.robot.arm.move_IK_target('ik_target.robot.arm.kuka_7', [cx+x3,cy+y3,cz+z3], [0.0,0.0,0.0], False, 1,1 )
        # simu.robot.arm.place_IK_target('ik_target.robot.arm.kuka_7', [cx+x3,cy+y3,cz+z3], [0.0,0.0,0.0], False )
        print(simu.robot.arm.probeviz.get_local_data())

        simu.sleep(3)
        simu.robot.arm.move_IK_target('ik_target.robot.arm.kuka_7', [cx+x4,cy+y4,cz+z4], [0.0,0.0,0.0], False, 1,1 )
        # simu.robot.arm.place_IK_target('ik_target.robot.arm.kuka_7', [cx+x4,cy+y4,cz+z4], [0.0,0.0,0.0], False)
        print(simu.robot.arm.probeviz.get_local_data())

# def probe_value():
#     with pymorse.Morse() as simu:
#         simu.robot.arm.probeviz.subscribe(probedata)
#         # simu.robot.arm.armpose.subscribe(print_pos)
#         while True:
#             # simu.robot.arm.probeviz.get_local_data()
#             # simu.robot.arm.probeviz.subscribe(probedata)
#             # simu.robot.arm.probeviz.publish({"test": 45})
# # set_horizontal()


moveTo4corners()



# list_scan_limits()
# startScan()

# jump_to_new_scan()