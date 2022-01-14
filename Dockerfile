FROM nvcr.io/nvidia/l4t-ml:r32.6.1-py3
RUN echo "Build our Container based on L4T Pytorch"
RUN nvcc --version

COPY requirements.txt .
COPY src ./src
COPY datasets ./datasets
COPY osnet_ain_x0_25_imagenet.pyth .

#RUN apt-get update && apt-get -y upgrade \
#  && apt-get install -y --no-install-recommends \
#    git \
#    wget \
#    g++ \
#    ca-certificates \
#    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -U \
        pip \
        setuptools \
        wheel

RUN git clone https://github.com/KaiyangZhou/deep-person-reid.git

RUN pip3 install -r /deep-person-reid/requirements.txt

RUN pip3 install --upgrade torch

#ENV QT_DEBUG_PLUGINS 1
ENV QT_QPA_PLATFORM_PLUGIN_PATH /usr/local/lib/python3.6/dist-packages/cv2/qt/plugins/platforms

# inside the docker container cli:
# cd deep-person-reid && /
# python3 setup.py develop && /
# python3 /src/opencv_gui.py

ENTRYPOINT ["/bin/bash"]