# ref1: https://aleksandarhaber.com/how-to-create-and-run-ros2-packages-in-docker-containers-from-scratch/
# ref2: https://automaticaddison.com/the-complete-guide-to-docker-for-ros-2-jazzy-projects/#Write_a_Dockerfile_From_Scratch

ARG ROS_DISTRO=humble

# use humble image for jammy (ubuntu 22)
FROM osrf/ros:${ROS_DISTRO}-desktop

ENV ROS_DISTRO=${ROS_DISTRO}
ENV WORKSPACE=pioneer_test_ws

SHELL ["/bin/bash", "-c"]

WORKDIR /app

COPY src ${WORKSPACE}/src

# RUN addgroup --gid 1000 user && \
#     adduser --uid 1000 --gid 1000 --home /${WORKSPACE} --disabled-password --gecos "" user

# upgrade system and install essential tools
RUN apt-get update -q && \
    apt-get upgrade -yq && \
    apt-get install -yq --no-install-recommends apt-utils wget curl git build-essential \
    vim sudo lsb-release locales bash-completion x11-apps xauth

# # gui:
# RUN apt-get update && apt-get install -y \
#     libx11-xcb1 libxcb1 libxcb-render0 libxcb-shape0 \
#     libxcb-xfixes0 libxcb-xinerama0 libxrender1 \
#     libxi6 libgl1-mesa-glx libxrandr2 x11-apps

# install tools to assist with ros development
RUN apt-get install -y iputils-ping usbutils \
    python3-argcomplete python3-colcon-common-extensions python3-pip python3-rosdep python3-vcstool

# set up the ROS 2 environment
RUN rosdep update && \
    echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> /root/.bashrc
    
# install ROS 2 packages
RUN apt-get install -y \
    # put packages below:
    ros-${ROS_DISTRO}-rviz2 \
    ros-${ROS_DISTRO}-sick-scan-xd

# install mesa graphics drivers for graphics (like rviz)
RUN apt-get install -y software-properties-common && \
    add-apt-repository ppa:kisak/kisak-mesa
    
# install any dependencies
RUN source /opt/ros/${ROS_DISTRO}/setup.bash && \
    rosdep update && \
    rosdep install --from-paths ${WORKSPACE}/src --ignore-src --rosdistro ${ROS_DISTRO} -y

# help keep image size down by clearing caches
RUN apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# build and source workspace
RUN cd ${WORKSPACE} && \
    colcon build && \
    source /app/${WORKSPACE}/install/setup.bash

# add and execute entry point
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# USER 1000:1000

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/bin/bash"]