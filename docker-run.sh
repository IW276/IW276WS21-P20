xhost +local:docker
docker run --rm \
          -e DISPLAY \
          -v /tmp/.X11-unix:/tmp/.X11-unix \
          reid_p20_final
