#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image

ROS_NODE_NAME = "image_processing_node"
photo_state = ""

def update_state(state_bool):
    global photo_state
    if photo_state == "":
        photo_state = state_bool.data
    #print(photo_state)

def img_process(img):
    global photo_state
    #rospy.loginfo("image width: %s height: %s" % (img.width, img.height))
    frame = np.ndarray(shape=(img.height, img.width, 3), dtype=np.uint8, buffer=img.data)
    cv2_img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    #cv2.rectangle(cv2_img, (5, 5), (635, 475), (0, 255, 0), 5)
    cv2.imshow("Frame", cv2_img)
    #print(photo_state)
    if photo_state == "1":
        cv2.imwrite("selfie.jpg", cv2_img)
        print("S-a salvat")
        photo_state = ""
    cv2.waitKey(1)

def cleanup():
    rospy.loginfo("Shutting down...")
    cv2.destroyWindow("Frame")

if __name__ == "__main__":
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.INFO)
    rospy.on_shutdown(cleanup)
    rospy.Subscriber("/usb_cam/image_raw", Image, img_process)
    rospy.Subscriber("/my_subscriber/my_topic", String, update_state)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass
