import rclpy
from rclpy.node import Node
from Phidget22.Phidget import *
from Phidget22.Devices.Accelerometer import *
from Phidget22.Devices.Gyroscope import *
import time

class ImuTestNode(Node):
	def __init__(self):
		super().__init__("imu_test_node")
		
		self.get_logger().info("IMU Test Node Initialized")
		
		# Initialise sensors
		self.accelerometer0 = Accelerometer()
		self.gyroscope0 = Gyroscope()

		self.timer = self.create_timer(1.0, self.timer_callback)

		self.accelerometer0.setOnAccelerationChangeHandler(onAccelerationChange)
		self.gyroscope0.setOnAngularRateUpdateHandler(onAngularRateUpdate)

		self.accelerometer0.openWaitForAttachment(5000)
		self.gyroscope0.openWaitForAttachment(5000)
	
	def timer_callback(self):
		self.get_logger().info("Timer triggered")


	def shutdown_handler(self):
		self.get_logger().info("IMU Test Node is shutting down")
		
		self.accelerometer0.close()
		self.gyroscope0.close()

		self.timer.cancel()

def onAccelerationChange(self, acceleration, timestamp):
	print("Acceleration: \t"+ str(acceleration[0])+ "  |  "+ str(acceleration[1])+ "  |  "+ str(acceleration[2]))
	print("Timestamp: " + str(timestamp))

def onAngularRateUpdate(self, angularRate, timestamp):
	print("AngularRate: \t"+ str(angularRate[0])+ "  |  "+ str(angularRate[1])+ "  |  "+ str(angularRate[2]))
	print("Timestamp: " + str(timestamp))

def main(args=None):
	rclpy.init(args=args)
	node = ImuTestNode()
	try:
		rclpy.spin(node)
	finally:
		node.shutdown_handler()
		node.destroy_node()
		rclpy.shutdown()

if __name__ == '__main__':
	main()
