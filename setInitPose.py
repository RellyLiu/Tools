#!/usr/bin/env python
from agv_msgs.srv import SetRobotInitPose, SetRobotInitPoseRequest, controlDoor, controlDoorRequest
from agv_msgs.msg import controlDoorInfo
import rospy
import random


if __name__ == '__main__':
    rospy.init_node('correct_location', anonymous=False)
    rospy.loginfo("init node ok")
    r = rospy.Rate(0.02)

    try:
        rospy.wait_for_service('/nav_monitor/set_init_pose')
        set_init_pose = rospy.ServiceProxy(
                '/nav_monitor/set_init_pose', SetRobotInitPose)
        open_door = rospy.ServiceProxy('AccessControl/control', controlDoor)

        count = 0
        while not rospy.is_shutdown():
            
            open = controlDoorInfo()
            open.control_type = 1
            open.doorId = '9999'
            controlOpen = controlDoorRequest()
            controlOpen.doorInfoList.append(open)
            result = open_door(controlOpen)
            rospy.loginfo("open door result: %x", result.result)
        
            pose = SetRobotInitPoseRequest()
            pose.pose_x = random.randint(0,9) * 0.1 + 200720
            pose.pose_y = random.randint(0,9) * 0.1 + 80193
            pose.pose_theta = 90000
            #pose.width = 2000
            #pose.height = 2000
            #pose.isFromNav = false
            result = set_init_pose(pose)
            ret = result.result
            rospy.loginfo("set init count %d, result: %x" % (count, ret))

            close = controlDoorInfo()
            close.control_type = 2
            close.doorId = '9999'
            controlClose = controlDoorRequest()
            controlClose.doorInfoList.append(close)
            result = open_door(controlClose)
            rospy.loginfo("close door result: %x", result)

            r.sleep()
 
    except rospy.ServiceException, e:
        print "set init pose call failed:%s" % e
