#!/usr/bin/env python3
import rospy
from sensor.msg import Led, RGB

def fun():
    rospy.logdebug("Hello from the other side!")

colours = [[255,0,0],[255,255,255],[0,0,255]]

if __name__ == "__main__":
    rospy.init_node("HELLO", log_level = rospy.DEBUG)
    print("hello world!")
    rate = rospy.Rate(3)
    rospy.on_shutdown(fun)
    p = rospy.Publisher("sensor/rgb_led", Led, queue_size = 1)
    i = 0
    while not rospy.is_shutdown():
        rospy.loginfo("ne place aici!")
        p.publish(Led(index = 0, rgb = RGB(r = colours[i%3][0], g = colours[i%3][1], b = colours[i%3][2])))
        rate.sleep()
        i = i + 1

