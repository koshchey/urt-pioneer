# ref1: https://aleksandarhaber.com/how-to-create-and-run-ros2-packages-in-docker-containers-from-scratch/
# ref2: https://automaticaddison.com/the-complete-guide-to-docker-for-ros-2-jazzy-projects/#Write_a_Dockerfile_From_Scratch

ARG ROS_DISTRO=humble

FROM osrf/ros:${ROS_DISTRO}-desktop

ENV ROS_DISTRO=${ROS_DISTRO}
ENV WORKSPACE=pioneer_ws

SHELL ["/bin/bash", "-c"]

WORKDIR /app

RUN useradd -ms /bin/bash pioneer

USER root

RUN apt-get update -q && \
    apt-get upgrade -yq && \
    apt-get install -yq --no-install-recommends apt-utils wget curl git build-essential \
    vim sudo lsb-release locales bash-completion x11-apps xauth

RUN apt-get install -y iputils-ping usbutils \
    python3-argcomplete python3-colcon-common-extensions python3-pip python3-rosdep python3-vcstool

RUN rosdep update && \
    echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> /root/.bashrc 

# ROS 2 packages
RUN apt-get install -y \
    ros-${ROS_DISTRO}-rviz2 \
    ros-${ROS_DISTRO}-sick-scan-xd \
    ros-${ROS_DISTRO}-depthai-ros \
    # ros-${ROS_DISTRO}-depthai-ros-driver \
    ros-${ROS_DISTRO}-rtabmap-ros

RUN apt-get install -y software-properties-common && \
    add-apt-repository ppa:kisak/kisak-mesa

# RUN source /opt/ros/${ROS_DISTRO}/setup.bash && \
#     rosdep update && \
#     rosdep install --from-paths ${WORKSPACE}/src --ignore-src --rosdistro ${ROS_DISTRO} -y

RUN apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy our packages
COPY src ${WORKSPACE}/src

RUN cd ${WORKSPACE} && \
    colcon build && \
    source /app/${WORKSPACE}/install/setup.bash

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

#COPY --chown=pioneer:pioneer --chmod=700 . ${WORKSPACE}
RUN chown -R pioneer ${WORKSPACE}
RUN gpasswd --add pioneer dialout

USER pioneer

#RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> /root/.bashrc 

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/bin/bash"]