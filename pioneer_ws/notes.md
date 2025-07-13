## Notes

## Docker
Remove dangling images (indicated as <none>:<none> though not all these may be dangling):
`docker rmi $(docker images -f "dangling=true" -q)`

## Lidar
Package:`ros-humble-sick_scan_xd`
Launch lidar with (point cloud stored in /scan):
`ros2 launch sick_scan_xd sick_tim_7xx.launch.py`

## Depth Camera:
Package: `ros-humble-depthai-ros-driver`

1. Follow this guide for camera itself (basically just step 1) (install on host):
https://docs.luxonis.com/hardware/platform/deploy/usb-deployment-guide/

2. Get the driver:
https://docs.luxonis.com/software/ros/depthai-ros/

(Go to DepthAI ROS -> Driver for launch examples.
To see stereo example in RVIZ use:
`ros2 launch depthai_examples stereo.launch.py`
Camera only:
`ros2 launch depthai_ros_driver camera.launch.py`)

**Repo** for ROS 2: https://github.com/luxonis/depthai-ros

Examples: https://github.com/luxonis/depthai-ros/tree/humble/depthai_examples
Launch files: https://github.com/luxonis/depthai-ros/tree/humble/depthai_ros_driver/launch

## Real Time Appearance Based (RTAB) Mapping
RTAB-Map: https://introlab.github.io/rtabmap/
**Repo** for ROS 2: https://github.com/introlab/rtabmap_ros

Demos: https://github.com/introlab/rtabmap_ros/tree/ros2/rtabmap_demos#rtabmap_demos
Examples: https://github.com/introlab/rtabmap_ros/tree/ros2/rtabmap_examples/launch
