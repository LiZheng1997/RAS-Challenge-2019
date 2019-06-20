#!/usr/bin/env python

# KUKA API for ROS

# Marhc 2016 Saeid Mokaram  saeid.mokaram@gmail.com
# Sheffield Robotics    http://www.sheffieldrobotics.ac.uk/
# The university of sheffield   http://www.sheffield.ac.uk/

# This script generats a ROS node for comunicating with KUKA iiwa
# Dependencies: conf.txt, ROS server, Rospy, KUKA iiwa java SDK, KUKA iiwa robot.

# This application is intended for floor mounted robots.
#######################################################################################################################

#!/usr/bin/env python
import sys
import re
import rospy
import moveit_commander
from std_msgs.msg import String
from moveit_msgs.msg import PickupAction, Grasp, CollisionObject, RobotState, MoveGroupActionFeedback
from geometry_msgs.msg import Pose, PoseStamped, Quaternion
from shape_msgs.msg import SolidPrimitive
from sensor_msgs.msg import JointState
from math import pi, radians, degrees
from actionlib import SimpleActionClient
from tf.transformations import *
import readchar
import subprocess as sp
from client_lib import *




class PickPlace():

	def __init__(self):
		try:
			# Initializing the node
			moveit_commander.roscpp_initialize(sys.argv)
			rospy.init_node('iiwa_pick_place', anonymous=False)
			move_group = "manipulator"
			self.sim = rospy.get_param("/simulation")

			# Instantiating a Robot Commander
			self._robot = moveit_commander.RobotCommander()

			# Instantiating a Scene
			self._scene = moveit_commander.PlanningSceneInterface()

			# Instantiating a Move Group
			self._move_group = moveit_commander.MoveGroupCommander(move_group)

			# Publisher for Kuka API
			self._kuka_api_pub = rospy.Publisher('/moveit_iiwa', String, queue_size=10)

			# Predefined poses used for the 'pick and place' demo
			self._pose_over_tools = self.create_pose(0.999, -0.000, -0.001, 0.045, 0.365, 0.164, 0.623)
			self._pose_to_tools = self.create_pose(0.999, -0.001, -0.001, 0.045, 0.365, 0.155, 0.525)
			self._pose_place_away = self.create_pose(0.999, 0.000, -0.001, 0.045, 0.687, 0.143, 0.385)
			self._pose_place_table = self.create_pose(0.999, 0.000, -0.001, 0.045, 0.687, 0.143, 0.285)
			self._pose_home = self.create_pose(-0.000, 0.000, 0.000, 1.000, 0.000, 0.000, 1.306)

		except:
			print("An error occured. Make sure you are running MoveIt simulation first!")
			print('Exiting application')
			rospy.sleep(2)
			#sys.exit()

	def move_to_home_position():


if __name__ == '__main__':
	
	# Making a connection object.
	my_client = kuka_iiwa_ros_client()

	# Wait until iiwa is connected zzz!
	while (not my_client.isready): pass
	print('Started!')

	# Initializing Tool 1
	my_client.send_command('setTool tool1')
	

	# Initializing
	my_client.send_command('setJointAcceleration 1.0')  # If the JointAcceleration is not set, the defult value is 1.0.
	my_client.send_command('setJointVelocity 1.0')      # If the JointVelocity is not set, the defult value is 1.0.
	my_client.send_command('setJointJerk 1.0')          # If the JointJerk is not set, the defult value is 1.0.
	my_client.send_command('setCartVelocity 10000')     # If the CartVelocity is not set, the defult value is 100


	

	#This is a test to move the arm to left or right
	# Move close to a start position.
	my_client.send_command('setPosition 0 49.43 0 -48.5 0 82.08 0')


	# Move to the exact start position.
	my_client.send_command('setPositionXYZABC 700 0 300 -180 0 -180 ptp')  # ptp motions move with setJointAcceleration


	# Performing three lin motions with max posible speed.
	my_client.send_command('setPositionXYZABC 500 100 400 - - - lin')  # lin motions move with CartVelocity
	my_client.send_command('setPositionXYZABC - -100 350 - - - lin')
	my_client.send_command('setPositionXYZABC 700 0 300 - - - lin')


	# Performing same motion slower (CartVelocity 50mm/s')
	my_client.send_command('setCartVelocity 50') # This only controls the lin motions.

	my_client.send_command('setPositionXYZABC 500 100 400 - - - lin')  # lin motions move with CartVelocity
	my_client.send_command('setPositionXYZABC - -100 350 - - - lin')
	my_client.send_command('setPositionXYZABC 700 0 300 - - - lin')