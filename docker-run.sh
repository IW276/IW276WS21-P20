xhost +local:docker
docker run --rm \
          -e DISPLAY \
          -v /tmp/.X11-unix:/tmp/.X11-unix \
          reid_P20_final \
          "cd /deep-person-reid && python3 setup.py develop && cd /src"