#!/bin/bash

docker run -it --rm \
    --privileged \
    -e DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
    --net=host \
    pioneer-test