import pymorse
import random



def scanArea():
    ax1 = random.random()
    ax2 = random.random()
    limitax1 = -2.0    
    limitAX1 = 2.0
    limitax2 = -1.57
    limitAX2 = 1.57
    # axe1 = (abs(limitax1) - abs(limitAX1))*ax1 + limitax1
    # axe2 = (abs(limitax2) - abs(limitAX2))*ax2 + limitax2
    axe1 = ax1 * 2
    axe2 = ax2 * 1
    print(axe1,axe2)
    with pymorse.Morse() as simu:
        # goto start axis 1&2
        simu.robot.arm.set_rotation("kuka_1",axe1)
        simu.sleep(1)
        simu.robot.arm.set_rotation("kuka_2",axe2)
        # start scan
        for i in range(10):
            for j in range(10):
                simu.robot.arm.set_rotation("kuka_1",axe1 + i*0.03)
                simu.sleep(0.01)
                simu.robot.arm.set_rotation("kuka_2",axe2 + j*0.03)
                simu.sleep(0.01)

for x in range(100): 
    scanArea()