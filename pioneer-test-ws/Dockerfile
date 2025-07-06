# ref: https://aleksandarhaber.com/how-to-create-and-run-ros2-packages-in-docker-containers-from-scratch/
FROM osrf/ros:humble-desktop

SHELL ["/bin/bash", "-c"]

RUN useradd -ms /bin/bash ros

WORKDIR /app

COPY src pioneer-test-ws/src

RUN 
    # additional packages
    apt-get update \
    && wget install -y ros-humble-rviz2 \
    ros-humble-sick-scan-xd && \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    # dependencies
    rosdep update && \
    rosdep install --from-paths src --ignore-src --rosdistro humble -y && \
    # build
    rm -rf /var/lib/apt/lists/* && \
    source /opt/ros/humble/setup.bash && \
    colcon build --symlink-install

COPY --chown=ros ros_entrypoint.sh /ros_entrypoint.sh
RUN chmod +x  /ros_entrypoint.sh
ENTRYPOINT ["/ros_entrypoint.sh"]

USER ros

RUN ./entrypoint.sh

# docker build -t pioneer-test .
# docker run -it --rm pioneer-test:latest
# ros2 launch sick_scan_xd sick_tim_7xx.launch.py hostname:=192.168.0.1