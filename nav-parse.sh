#!/bin/bash
#########################################################################
# File Name: pose-parse.sh
# Author: Xiang Yu
# mail: xiang_yu@dahuatech.com
# Created Time: Monday, September 25, 2017 AM10:04:42 CST
#########################################################################

input=""
if [ $# != 1 ];
then
	echo "Example:"
	echo "	nav-parse agv_pose.sh"

	echo "use default /var/robot/log/nav/nav.log"
	input="/var/robot/log/nav/nav.log"
else
	input=$1
fi

#mode=`rosparam get /isDMCodeCamera`
mode=0
if [ $mode != 1 ];
then
    echo "解析激光导航日志..."
else
    echo "解析二维码导航日志..."
fi

TEMP_DIR=debug
TEMP_FILE=temp_nav.log
mkdir -p $TEMP_DIR
#去掉^@
perl -pe 's/\x0//g' $input > $TEMP_DIR/$TEMP_FILE
#删除最后一行
sed -i '$d' $TEMP_DIR/$TEMP_FILE
cd $TEMP_DIR

if [ $mode != 1 ];
then
#激光导航
    cat $TEMP_FILE |grep -v enml\] > noenml
    awk '/enml]/ {print $0}' $TEMP_FILE > enml
    awk '/monitor]/ {print $0}' noenml > monitor
    awk '/odom]/ {print $0}' noenml > odom
    awk '/move:/ {print $0}' odom > move
    awk '/pose:/ {print $1 " " $2  " " $5 " " $6 " " $7 " " $8 " " $9 " " $10 " " $11}' odom > pose
    awk '/pv:/ {print $1 " " $2  " " $6 " " $7}' noenml > vel
    awk '/get in add task/ {print "\n" $1 " " $2 " " $8 " " $9}
         /handleStartSpecialNav, taskId/ {print "\n" $1 " " $2 " " $5 " " $6}
         /task lock detail:|task detail:|task waypoint:|task result:|add task result:/ {$3="";$4="";print $0}
         /cancel task reason/ {print $1 " " $2 "   cancel " $8 }' monitor > task
else
    awk '/nav]/ {print $0}' $TEMP_FILE > nav
    awk '/get in add task|check error|task finished result|entry move waypoint/ {print $0}
         /recv way/ { gsub(/waypoint:[0-9]*,/, "");
	     if ($5 == "back")
		 $5 = "   back"
	     else if ($5 == "right")
		 $5 = "  right"
	     else if ($5 == "left")
		 $5 = "   left"
	     print $1 " " $2 " " $5 " " $19" "  $6 " " $7 " " $8 " " $9 " " $10}' nav > task
    awk '/pv/ {print $1 " " $2 " " $5 " " $6 " " $7 " " $8}' nav > vel
    awk '/pose]/ {print $0}' $TEMP_FILE > pose
    if [ ! -s pose ]
    then 
        cp nav pose
    fi
    awk '/] encoder:/ {print $1 " " $2 " " $5 " " $6 " " $7}' pose > encoder
    awk '/] imu:/ {print $1 " " $2 " " $5 " " $6}' pose > imu
    awk '/] dm:/  {print $1 " " $2 " " $5 " " $6 " " $7 " " $8 " " $9 " " $10 " " $11}' pose > dm
    awk '/dm adjust/  {print $0}' pose > dm_adjust
    awk '/odom:/ {print $1 " " $2 " "  $4 " " $5 " " $6 " " $7 " " $8 " " $9}' pose > odom
    awk '/move_status:/ {print $0}' pose > move
fi

awk '/yaw ex|reason=|fail:|brake|collision|turn not get point|get out|check error/ {print $0}' $TEMP_FILE > exception
awk '/secu]/ {print $0}' $TEMP_FILE > secu
