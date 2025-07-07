#!/bin/bash

set -e

distro=humble
workspace=pioneer_test_ws

export ROS_DOMAIN_ID=42

source /opt/ros/${distro}/setup.bash
cd ${workspace}
source install/setup.bash
colcon build
source install/setup.bash

exec "$@"