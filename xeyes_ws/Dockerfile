FROM ubuntu:22.04 as base

USER root
RUN apt-get update && \
    apt-get install -y wget \
    libx11-dev unzip sudo \
    xvfb x11vnc \
    python3 python3-pip \
    x11-apps 

RUN pip3 install numpy

RUN useradd -m xeyes

USER xeyes
WORKDIR /home/xeyes_ws
