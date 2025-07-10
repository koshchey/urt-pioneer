FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

USER root
# RUN apt-get update && \
#     apt-get install -y wget \
#     libx11-dev unzip sudo \
#     xvfb x11vnc \
#     python3 python3-pip \
#     x11-apps 
    
RUN apt-get update && apt-get install -qqy x11-apps

RUN useradd -m xeyes

USER xeyes
WORKDIR /home/xeyes_ws

# to run (make sure you use sudo):
# sudo docker run --rm -it --net=host --env DISPLAY=$DISPLAY ssh_image_tag_1
# or sudo docker compose up --no-start && sudo docker compose run --rm base