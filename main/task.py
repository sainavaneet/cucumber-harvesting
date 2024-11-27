from interbotix_xs_modules.arm import InterbotixManipulatorXS
import sys


def main():
    bot = InterbotixManipulatorXS("wx250", "arm", "gripper")

    if (bot.arm.group_info.num_joints < 5):
        print('This demo requires the robot to have at least 5 joints!')
        sys.exit()

    bot.arm.go_to_home_pose()
    bot.arm.set_ee_cartesian_trajectory(z=-0.2)
    bot.arm.set_ee_cartesian_trajectory(x=-0.2)
    bot.arm.set_ee_cartesian_trajectory(z=0.2)
    bot.arm.set_ee_cartesian_trajectory(x=0.2)
    bot.arm.go_to_sleep_pose()

if __name__=='__main__':
    main()
