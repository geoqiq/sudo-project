#!/usr/bin/env python3
import rospy
import cv2
import math
import numpy as np
import time
from std_srvs.srv import Empty
from puppy_control.msg import Pose, Gait, Velocity

ROS_NODE_NAME = "move_node"

pose_msg = Pose(roll=math.radians(0), pitch=math.radians(15), yaw=0, height=-10, x_shift=0, stance_x=0, stance_y=0, run_time=200)
pose_msg_stop = Pose(roll=math.radians(0), pitch=math.radians(0), yaw=0, height=-5, x_shift=0, stance_x=0, stance_y=0, run_time=200)

#pose_msg.x_shift = -0.6
#gait_msg = Gait(overlap_time=0.2, swing_time=0.3, clearance_time=0.0, z_clearance=5)

# amble
#pose_msg.x_shift = -0.9
#gait_msg = Gait(overlap_time=0.1, swing_time=0.2, clearance_time=0.1, z_clearance=5)

# walk
pose_msg.x_shift = -0.65
gait_msg = Gait(overlap_time=0.1, swing_time=0.2, clearance_time=0.3, z_clearance=5)

vel_msg = Velocity(x=0, y=0, yaw_rate=math.radians(0))

def cleanup():
    rospy.loginfo("Shutting down...")
    rospy.ServiceProxy("/puppy_control/go_home", Empty)()

if __name__ == "__main__":
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)
    rospy.on_shutdown(cleanup)
    rospy.ServiceProxy("/puppy_control/go_home", Empty)()
    pose_pub = rospy.Publisher("/puppy_control/pose", Pose, queue_size=1)
    gait_pub = rospy.Publisher("/puppy_control/gait", Gait, queue_size=1)
    vel_pub = rospy.Publisher("/puppy_control/velocity", Velocity, queue_size=1)

    gait_pub.publish(gait_msg)
    time.sleep(0.2)
    pose_pub.publish(pose_msg)
    time.sleep(0.2)

    i = 0
    while not rospy.is_shutdown():
        i = i + 1
        if i < 10:
            vel_msg.x = 10
            vel_msg.yaw_rate = math.radians(0)
        else:
            vel_msg.x = 0
            vel_msg.yaw_rate = 0
        vel_pub.publish(vel_msg)
        time.sleep(1)
        if i >= 10:
            pose_pub.publish(pose_msg_stop)
            time.sleep(0.2)
            break
