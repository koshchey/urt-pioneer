#!/bin/bash

set -e

distro=humble

export ROS_DOMAIN_ID=42

source /opt/ros/${distro}/setup.bash
source /app/pioneer-test-ws/install/setup.bash
colcon build
source /app/pioneer-test-ws/install/setup.bash

exec "$@"