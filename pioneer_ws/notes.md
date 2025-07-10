## Notes

## Docker
Remove dangling images (indicated as <none>:<none> though not all these may be dangling):
`docker rmi $(docker images -f "dangling=true" -q)`

## Lidar
Launch lidar with (point cloud stored in /scan):
`ros2 launch sick_scan_xd sick_tim_7xx.launch.py`

## Camera:
Follow this guide for camera itself (basically just step 1) (install on host):
https://docs.luxonis.com/hardware/platform/deploy/usb-deployment-guide/

Get the driver (install using Dockerfile):
https://docs.luxonis.com/software/ros/depthai-ros/

Go to DepthAI ROS -> Driver for launch examples

To see stereo example in RVIZ use:
`ros2 launch depthai_examples stereo.launch.py`

Camera only:
`ros2 launch depthai_ros_driver camera.launch.py`

Examples/launch files on: https://github.com/luxonis/depthai-ros/tree/humble/depthai_examples
and: https://github.com/luxonis/depthai-ros/tree/humble/depthai_ros_driver/launch

