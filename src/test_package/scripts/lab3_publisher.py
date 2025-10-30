#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

ROS_NODE_NAME = "my_publisher"

def emit():
    my_publisher = rospy.Publisher("/my_subscriber/my_topic", String, queue_size=1)
    key = input()
    if key == 's':
        my_publisher.publish("1")

if __name__ == "__main__":
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.INFO)
    try:
        emit()
    except KeyboardInterrupt:
        pass
