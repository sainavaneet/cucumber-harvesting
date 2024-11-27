from interbotix_xs_modules.arm import InterbotixManipulatorXS
import numpy as np
from robot_utils import move_arms, torque_on, torque_off
import time

class CucumberHarvesting:
    def __init__(self, robot_name='puppet_left'):
        
        self.bot = InterbotixManipulatorXS("vx300s", "arm", "gripper", robot_name=robot_name , moving_time=5)



    def perform_harvest(self):
        torque_on(self.bot)
        time.sleep(3)
        self.bot.arm.set_ee_pose_components(x=0.3,z=0.3)

        time.sleep(2)
        self.bot.arm.go_to_sleep_pose() 


if __name__ == '__main__':
    cucumber_harvest = CucumberHarvesting()
    cucumber_harvest.perform_harvest()
